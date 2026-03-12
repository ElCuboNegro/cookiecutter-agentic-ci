import os
import json
import re
import argparse
from collections import defaultdict

def extract_deps_package_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            deps = list(data.get('dependencies', {}).keys()) + list(data.get('devDependencies', {}).keys())
            return sorted(deps)
    except:
        return []

def extract_deps_requirements(path):
    try:
        deps = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('#')[0].strip()
                if line:
                    pkg = re.split(r'[=><~]', line)[0]
                    deps.append(pkg)
        return sorted(deps)
    except:
        return []

def cluster_projects(target_dir):
    clusters = defaultdict(list)
    
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', 'venv', '__pycache__', 'dist', 'build'}]
            
        if 'package.json' in files:
            deps = extract_deps_package_json(os.path.join(root, 'package.json'))
            if deps:
                sig = 'npm:' + ','.join(deps)
                clusters[sig].append(root)
                
        if 'requirements.txt' in files:
            deps = extract_deps_requirements(os.path.join(root, 'requirements.txt'))
            if deps:
                sig = 'pip:' + ','.join(deps)
                clusters[sig].append(root)
                
    return {sig: paths for sig, paths in clusters.items() if len(paths) > 1}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cluster projects by identical dependencies.')
    parser.add_argument('path', help='Path to scan')
    parser.add_argument('--out', default='deps_clusters.json', help='Output JSON file')
    args = parser.parse_args()
    
    print(f"Scanning {args.path} for duplicate project signatures...")
    clusters = cluster_projects(args.path)
    
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump({'clusters': clusters}, f, indent=2)
        
    print(f"Found {len(clusters)} clusters of projects with identical dependencies.")
    print(f"Report saved to {args.out}")
