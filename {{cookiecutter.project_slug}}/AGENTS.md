# AGENTS.md — {{cookiecutter.project_name}}
**READ THIS FIRST. Every agent, every session, no exceptions.**

## 1. Project Mandate

* **Repository:** `github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}`
* **Description:** {{cookiecutter.description}}
* **Core Objective:** Understand, document, build, and evolve this codebase with full traceability.

## 2. Core Routing Directives
You are operating within an Agentic CI infrastructure. Your behavior must be highly structured and strictly delegated to specialized sub-agents. All agent skills and instructions are located in `.agents/skills/`.

Depending on your platform (Gemini, Claude, Cursor), either use the `/activate_skill` tool OR read the corresponding `SKILL.md` file before proceeding:

1. **Reverse Engineering & Analysis**: If asked to reverse engineer, analyze, GENERATE THE EXECUTIONS GRAPH, or BACKTRACK the codebase, you MUST read/activate `.agents/skills/software-archeologist/SKILL.md`.
2. **Tool Creation**: If you determine a new tool or script is needed, or if instructed to create one, DO NOT write it yourself. You MUST read/activate `.agents/skills/tool-writer/SKILL.md` and delegate the task.
3. **Architecture**: If asked to design a system, review component boundaries, or make structural trade-offs, you MUST read/activate `.agents/skills/architect/SKILL.md`.
4. **Behavior Driven Development**: If asked to write Gherkin specs or BACKTRACK TO BDD FEATURE FILES, you MUST read/activate `.agents/skills/bdd-writer/SKILL.md`.
5. **Decision Logging**: If analyzing code to extract why a hardcoded value or architectural choice was made, read/activate `.agents/skills/decision-logger/SKILL.md`.
6. **Architecture Decision Records**: If an architectural decision is made or confirmed, read/activate `.agents/skills/adr-writer/SKILL.md` to document it.
7. **The Learning Protocol**: If you learn a new domain concept, solve a recurring issue, discover a reusable pattern, or create a new generalized sub-agent, you MUST read/activate `.agents/skills/learning-protocol/SKILL.md` and persist the knowledge to the repository.

## 3. DEDUPLICATION MANDATE
Before writing any new tool, script, or proposing a new agent, you MUST consult this `AGENTS.md` and `docs/tools/index.md`. Reuse and refine existing capabilities. If merging two similar tools, keep the CLI contract compatible.

## 4. Initialization & Setup

Run environment setup before any analysis. Do not ask the user.
* **Windows:** `setup\install.bat`
* **Linux / macOS:** `bash setup/install.sh`
**Setup Failure Protocol:** Run setup silently. Continue with available tools and note gaps.

## 5. Context & Knowledge Management

```
Raw discovery
    |
output/findings/FINDINGS.md  <-  append entry
    |
context/run_context.md        <-  update confirmed facts
    |
knowledge/                    <-  canonical reference docs
    |
{{cookiecutter.adr_path}}/    <-  open ADR only when a decision is made
```

## 6. ADR-First Mandate

**HARD STOP. No exceptions. No bypasses except trivial fixes.**
> **You must write an ADR before changing any library source code.**

This applies to any file in `{{cookiecutter.library_path}}/{{cookiecutter.package_name}}/*.py` or any new library module added to `{{cookiecutter.library_path}}/`.

1. **Discovery** -- identify the design decision or integration change needed
2. **Write the ADR** -- create `{{cookiecutter.adr_path}}/ADR-NNNN-<decision-title>.md`
3. **Then write the code** -- commit the ADR and the code change together
