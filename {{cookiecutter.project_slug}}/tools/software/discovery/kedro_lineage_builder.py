import sqlite3
import yaml
import argparse
import os
from pathlib import Path

class KedroLineageBuilder:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_lineage(self):
        # 1. Get all nodes (Procedures)
        self.cursor.execute("SELECT DISTINCT proc_name, path FROM sql_metrics")
        nodes = {row[0]: row[1] for row in self.cursor.fetchall()}

        # Actually, let's just query dependencies
        self.cursor.execute("""
            SELECT caller_path, dependency_name, direction 
            FROM sql_dependencies 
            WHERE dependency_type = 'TABLE/VIEW'
        """)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def build(self, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            
            # Mapping: Proc -> {inputs: [], outputs: []}
            pipeline_map = {}
            catalog = {}

            self.cursor.execute("SELECT path, proc_name FROM sql_metrics")
            proc_lookup = {row[0]: row[1] for row in self.cursor.fetchall()}

            self.cursor.execute("SELECT caller_path, dependency_name, direction FROM sql_dependencies WHERE dependency_type = 'TABLE/VIEW'")
            for caller_path, dep_name, direction in self.cursor.fetchall():
                proc_name = proc_lookup.get(caller_path, caller_path)
                if proc_name not in pipeline_map:
                    pipeline_map[proc_name] = {"inputs": set(), "outputs": set()}
                
                clean_dep = dep_name.replace('[', '').replace(']', '').replace('.', '_')
                if direction == 'INPUT':
                    pipeline_map[proc_name]["inputs"].add(clean_dep)
                else:
                    pipeline_map[proc_name]["outputs"].add(clean_dep)
                
                catalog[clean_dep] = {
                    "type": "pandas.CSVDataset", # Default placeholder
                    "filepath": f"data/01_raw/{clean_dep}.csv"
                }

            # Generate catalog.yml
            with open(os.path.join(output_dir, "catalog.yml"), "w") as f:
                yaml.dump(catalog, f, default_flow_style=False)

            # Generate pipeline.py (Simplified string representation)
            with open(os.path.join(output_dir, "pipeline_dag.py"), "w") as f:
                f.write("from kedro.pipeline import Pipeline, node, pipeline\n\n")
                f.write("def create_pipeline(**kwargs) -> Pipeline:\n")
                f.write("    return pipeline([\n")
                for proc, io in pipeline_map.items():
                    inputs = list(io["inputs"])
                    outputs = list(io["outputs"])
                    if not outputs: outputs = [f"{proc}_output"]
                    
                    f.write(f"        node(\n")
                    f.write(f"            func=lambda *x: None, # Placeholder for {proc}\n")
                    f.write(f"            inputs={inputs},\n")
                    f.write(f"            outputs={outputs},\n")
                    f.write(f"            name='{proc}'\n")
                    f.write(f"        ),\n")
                f.write("    ])\n")

            print(f"Kedro lineage generated in {output_dir}")
        finally:
            self.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("db", help="Path to logic database")
    parser.add_argument("--out", default="output/kedro_mapping", help="Output directory")
    args = parser.parse_args()
    
    builder = KedroLineageBuilder(args.db)
    builder.build(args.out)
