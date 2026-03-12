# Software Discovery Tools

**All manual discovery scripts have been removed.**

As per the **New Stack Mandate** in `AGENTS.md`, any tools required to parse, analyze, or build the executions graph for a specific stack must be dynamically built by the **Tool Writer Agent**. 

When an agent needs to perform software archeology, they must first generate generalizable analysis tools in this directory and iteratively improve them as they learn the new stack. Do not rely on legacy, hardcoded regex parsers.
