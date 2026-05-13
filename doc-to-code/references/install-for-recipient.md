# Install for Recipient

Use this guide when packaging `doc-to-code` for another Codex user.

## Zip Contents

The distributable zip should contain one top-level folder:

```text
doc-to-code/
  SKILL.md
  agents/openai.yaml
  references/
    deliverables.md
    gui-and-evidence.md
    install-for-recipient.md
    setup.md
    traceability.md
    workflow.md
```

Do not package generated project code, patent documents, private data, logs, or screenshots inside the skill zip unless the user explicitly asks for a separate project archive.

## Manual Installation

Tell the recipient to:

1. Extract the zip.
2. Copy the `doc-to-code` folder into their global Codex skills directory, usually `~/.codex/skills/`.
3. Confirm the folder contains `SKILL.md` directly inside `~/.codex/skills/doc-to-code/`.
4. Restart Codex so the skill metadata is loaded.
5. Invoke the skill with `$doc-to-code`.

## Dependency Check After Install

After restart, the recipient should confirm:

- At least one suitable `.docx` reader is installed and enabled.
- At least one suitable `.pdf` reader is installed and enabled.
- `fetch` MCP is available if external source fetching is needed.
- `duckduckgo` MCP is available if source discovery is needed.
- `$figma-generate-design` skill is installed.
- Local Conda is installed and callable.

If `$figma-generate-design` is missing and `skill-installer` is available, install it from the official `openai/skills` repository. If the required reading capability is missing, ask the recipient to install or enable any suitable DOCX/PDF-reading MCP in their Codex environment.

## Installation Boundary

The skill can tell Codex what to check and how to guide the user, but it cannot guarantee automatic installation on every machine. Installation depends on the recipient's Codex version, permissions, MCP availability, network access, and whether the recipient approves downloads or global configuration changes.

If a dependency is missing, Codex should report a clear missing-dependency list before continuing with reduced capability.
