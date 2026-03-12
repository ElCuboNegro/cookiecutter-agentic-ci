# Learning Log

This file tracks all abstract patterns, domain concepts, and generalized architectural rules learned by agents working in this repository.

## [2026-03-12] Learning: Self-Analysis of the Agentic Cookiecutter Template
- **Trigger**: The need to initialize the repository, fully document it, and test the learning protocol by using the cookiecutter set of agents to analyze the cookiecutter repo itself.
- **Action Taken**: 
  - Ran the `software-archeologist` protocol on the repository.
  - Generated the Findings Ledger (`docs/findings/FINDINGS.md`), capturing the fact that this is a templating structure, not a runtime codebase.
  - Mapped the architecture into `docs/archeology/index.md`.
  - Created the executions graph (`docs/archeology/executions-graph.dot`) detailing the templating and post-generation hook flow.
- **Impact**: Demonstrates that the provided Agentic CI tools and protocols (like the Software Archeologist and Learning Protocol) are capable of abstracting and analyzing not just target applications, but metaprogramming and infrastructure repositories like this Cookiecutter template. This validates the agentic loop and populates the repository's permanent knowledge base.

## [2026-03-12] Learning: The "New Stack" Tool Creation Mandate
- **Trigger**: An instruction to establish a standardized approach when agents encounter a completely new technology stack.
- **Action Taken**: 
  - Updated the `software-archeologist` protocol to mandate invoking the Tool Writer rather than relying on ad-hoc grepping.
  - Updated the `learning-protocol` to define the "New Stack Protocol" (Step 3), mandating the creation of generalizable tools first, followed by iterative improvement during experimentation.
- **Impact**: Forces agents to build long-term, reusable abstraction layers instead of hallucinating through brute-force manual analysis, significantly improving the scalability of the agentic CI system across disparate repositories.

## [2026-03-12] Learning: The General vs. Specific Knowledge Split
- **Trigger**: The need to ensure that knowledge generated across various developers and projects remains strictly reusable and unpolluted by project-specific artifacts.
- **Action Taken**: 
  - Updated the `software-archeologist` skill to explicitly define "The General vs. Specific Knowledge Split".
  - Clarified that tools, parsers, and extractors must be perfectly abstracted and belong in `tools/` (for upstream contribution to the cookiecutter).
  - Clarified that quirks, hardcoded constants, and API maps are project-specific findings and belong exclusively in `docs/knowledge/`.
  - Updated the `learning-protocol` to reflect that domain knowledge documentation is bound to the local project and must never be hardcoded into the general tools.
- **Impact**: Guarantees that the cookiecutter template's upstream tools remain universally applicable to any codebase, while simultaneously ensuring that local projects retain their highly specific archaeological findings.
