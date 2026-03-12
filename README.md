# cookiecutter-agentic-ci

A comprehensive [cookiecutter](https://cookiecutter.readthedocs.io/) template that scaffolds a Python project with a complete **Agentic CI/CD infrastructure**, an **ADR-first mandate**, and a rich set of **AI agent skills** (including Software Archeologist and Learning Protocol). 

This template is designed to force AI coding assistants (like Gemini, Claude, and Cursor) to follow strict architectural guidelines, log their decisions, reverse-engineer code properly, and enforce architectural constraints in CI.

## 🚀 Features & Architecture

This cookiecutter provides a unified Agentic CI infrastructure governed by `AGENTS.md`. When generated, your project will contain:

### Core Agent Directives
- `AGENTS.md`: The single source of truth for all AI agents working in the repository. It defines routing directives, the discovery process, and the ADR mandate.
- `CLAUDE.md`, `GEMINI.md`, `.cursorrules`: Agent-specific entry points that import and enforce the rules defined in `AGENTS.md`.

### AI Agent Skills
Located in `.agents/skills/`, these are specialized markdown protocols that AI agents must read or activate when performing specific tasks:
- **`adr-writer`**: Documents architectural decisions.
- **`architect`**: Designs systems and reviews component boundaries.
- **`bdd-writer`**: Writes Gherkin specs and backtracks to BDD feature files.
- **`code-reviewer`**: Reviews code for quality and security.
- **`decision-logger`**: Analyzes code to extract why hardcoded values or architectural choices were made.
- **`learning-protocol`**: The crucial protocol for when an agent learns a new domain concept or solves a recurring issue. It dictates how to persist knowledge back into the repository.
- **`software-archeologist`**: Used for reverse-engineering, generating execution graphs, and backtracking the codebase.
- **`tool-writer`**: Used when an agent determines a new tool or script is needed.
- **`unknown-domain-protocol`**: Guidelines for when an agent encounters unfamiliar concepts.

### The ADR-First Mandate
Any change to the core library source code requires a new Architecture Decision Record (ADR).
- **CI Gate (`tools/check_adr_gate.py`)**: A Python script that enforces the ADR mandate automatically in CI.
- **GitHub Actions (`.github/workflows/ci.yml`)**: A workflow that runs the ADR gate and test jobs on every Pull Request.

## 📦 Quickstart

```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Generate a new project from this template
cookiecutter gh:deagentic/cookiecutter-agentic-ci
```

Or from a local copy:

```bash
cookiecutter path/to/cookiecutter-agentic-ci
```

## ⚙️ Template Variables

During generation, you'll be prompted to fill in these variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `project_name` | My Project | Human-readable project name |
| `project_slug` | my-project | Repo / directory name (kebab-case) |
| `package_name` | my_package | Python package name (snake_case) |
| `github_username` | myuser | GitHub username or organization |
| `description` | ... | One-line project description |
| `author` | Your Name | Author name |
| `python_version` | 3.11 | Minimum Python version for CI |
| `library_path` | library | Subdirectory containing the Python package |
| `adr_path` | docs/adr | Subdirectory for ADR files |

## 🛠️ Post-Generation

After generating your project:
1. `cd <project_slug>`
2. Open `docs/adr/index.md` and write `ADR-0001` to establish the initial project architecture.
3. Push to GitHub! The ADR gate will run automatically on every PR to ensure AI agents (and humans) are documenting their architectural decisions.

## 🧠 The Learning Protocol (Self-Analysis)

This template includes a specific `learning-protocol` skill. When an AI agent operating within the generated project learns something new or solves a complex recurring issue, it is instructed by `AGENTS.md` to use this protocol to persist that knowledge into the repository's `knowledge/` directory, ensuring the AI system gets smarter over time.
