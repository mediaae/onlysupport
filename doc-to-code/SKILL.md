---
name: doc-to-code
description: Convert patent, invention-disclosure, technical DOCX/PDF, and evidence documents into a rigorously implemented software prototype with traceable code, test cases, runtime outputs, data displays, a Conda-based local environment, and a required GUI-style frontend demonstration interface. Use when Codex must read legal or technical documents through any available DOCX/PDF-capable MCP or equivalent file-reading tool, extract enforceable requirements, implement code that strictly follows the source text, use the user's local Conda environment named from the patent project, use figma-generate-design only for GUI design, and prepare patent proof materials from the implemented code and tests with high correctness standards.
---

# Doc to Code

## Operating Standard

Treat the source documents as authoritative. Do not invent algorithms, data flows, UI claims, or proof points that are not grounded in the patent materials or explicit user instructions. The patent proof material is the implemented code, test samples, runtime results, logs, data traces, and traceability evidence. The GUI is a distinctive presentation and interaction layer, not the primary proof artifact. When the documents are ambiguous, record the ambiguity and ask for confirmation before turning it into behavior.

Before coding, verify the required capabilities are available:

- A `.docx`-capable reader. Prefer an MCP that can expose headings, paragraphs, tables, comments, tracked changes, images, and document properties. `word-expert` is one example, not a hard requirement.
- A `.pdf`-capable reader. Prefer an MCP that can expose page-level text, OCR warnings, claims, figures, tables, captions, and scanned/structured extraction details. `pdf-mcp-pro` is one example, not a hard requirement.
- `fetch` and `duckduckgo` MCP are recommended only when current public information, source lookup, or official documentation lookup is needed.
- `$figma-generate-design` skill for GUI concept generation and design handoff. If missing, install it with `skill-installer` from `openai/skills`.
- The user's local Conda installation for project virtual environment creation and dependency isolation.
- Any project-specific test, build, GUI, or database tools already present in the repository.

Read `references/setup.md` before starting when the environment, MCP servers, or required skills may be missing. Read `references/workflow.md` for the complete execution sequence. Read `references/traceability.md` whenever implementing or reviewing code against patent claims. Read `references/gui-and-evidence.md` before designing the interface. Read `references/deliverables.md` before packaging final proof artifacts. Read `references/install-for-recipient.md` when preparing the skill for distribution to another Codex user.

## Required Workflow

1. Ingest all provided patent, disclosure, PDF, DOCX, data, and project files. Preserve filenames, page/paragraph references, claim numbers, figures, tables, and user notes.
2. Build or select a local Conda environment named from the patent project. Record the environment name, Python/runtime version, and dependency install commands.
3. Build a traceability matrix before implementation. Map each claim or technical requirement to source location, interpretation, planned code module, test sample, runtime output, and data evidence.
4. Implement only what the documents support. Keep code clear, deterministic, tested, and reviewable. Prefer existing project architecture and dependencies.
5. Design and implement a unique GUI-style frontend demonstration interface with `$figma-generate-design` after the functional requirements are stable. The GUI must make the implemented patented mechanism understandable and must not be treated as a substitute for code or tests.
6. Add data displays that expose the mechanism: inputs, intermediate states, outputs, comparisons, metrics, logs, or visualizations as appropriate for the patent. The underlying code paths and test samples are the proof material.
7. Verify with build, lint, typecheck, tests, GUI smoke tests, and manual review. Fix all errors introduced by the work.
8. Deliver concise evidence: what was implemented, which Conda environment was used, how the code maps to the patent, what tests passed, what artifacts were produced, and any unresolved ambiguities.

## Quality Gates

Do not mark the task complete until:

- Every implemented feature maps to a source document reference or explicit user instruction.
- Every patent claim selected for implementation has code evidence, test samples, and runtime or data evidence.
- The implementation uses a documented local Conda environment whose name is derived from the patent project.
- The GUI frontend is original, domain-specific, runnable, and useful for demonstration, but proof claims remain grounded in code and tests.
- Final delivery includes the required deliverables checklist from `references/deliverables.md`.
- No known build, runtime, lint, type, or test errors remain from the implementation.
- Any unsupported or ambiguous patent language is documented instead of silently guessed.

## MCP Notes

Prefer the strongest available document-reading path in this order:

1. A document MCP that exposes the needed structure for the file type.
2. Another MCP or built-in tool that can still extract the required text and structural anchors.
3. A local parser or fallback reader, but only after recording what fidelity is lost.

If no available tool can expose the document structure needed for faithful implementation, tell the user exactly which capability is missing, what evidence may be unreliable, and whether you can continue with reduced confidence. The skill can guide Codex to remind users and attempt installation where supported, but automatic installation depends on the recipient's Codex environment, permissions, available `skill-installer`, and whether each MCP can be installed from an accessible source. If the document contains confidential or legal material, avoid unnecessary web search and keep analysis grounded in local files.
