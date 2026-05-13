# Setup and Dependency Checks

Use this guide before running `doc-to-code` in a new Codex environment.

## Required MCP Servers

- At least one `.docx`-capable reader is required for DOCX patent drafts. Prefer an MCP that can expose comments, tracked changes, tables, footnotes, endnotes, images, and document properties. `word-expert` is a strong example, but not mandatory.
- At least one `.pdf`-capable reader is required for patent PDFs. Prefer an MCP that can expose scanned or structured extraction details, page-level references, claims, figures, tables, and OCR warnings. `pdf-mcp-pro` is a strong example, but not mandatory.

If the required reading capability is missing or disabled, stop and tell the user exactly what is unavailable. Ask the user to enable or install a suitable MCP before claiming high-confidence document extraction.

## Recommended MCP Servers

- `fetch`: Recommended when official documentation or a specific source page must be fetched.
- `duckduckgo`: Recommended when source discovery or current public information is needed.

Use recommended MCP servers only when they improve the task. For confidential patent work, avoid unnecessary web access.

## Required Skill

- `$figma-generate-design`: Required for GUI design generation and design handoff after the patent requirements, implementation plan, and traceability matrix are stable.

If `$figma-generate-design` is missing, try the local `skill-installer` workflow if available:

1. List installable skills from `openai/skills`.
2. Select `figma-generate-design`.
3. Install it into the recipient's global Codex skills directory.
4. Tell the user to restart Codex so the new skill is loaded.

If `skill-installer` is unavailable, tell the user that `figma-generate-design` must be installed manually from the official `openai/skills` repository before GUI design work can use that skill.

## Required Local Conda Environment

Use the user's local Conda installation for virtual environment construction. Do not silently create a generic `.venv` unless the user explicitly approves a fallback because Conda is unavailable.

Derive the environment name from the patent project:

1. Identify the project name from the patent title, invention name, repository name, or user-provided project name.
2. For Chinese titles, prefer a concise pinyin slug or an English project alias derived from the user's wording, patent abstract, or repository name.
3. If the project name is long, numbered, confidential, multilingual, or unclear, ask the user to confirm a short project alias before creating the environment.
4. Normalize it to a short Conda-safe slug: lowercase ASCII, words separated by hyphens, remove punctuation, no spaces, no Chinese characters, and keep it under 48 characters.
5. Use only characters that are safe for Conda and shell commands: `a-z`, `0-9`, and hyphens.
6. Prefix it with `patent-` unless the user provides a naming convention.
7. Example: `Adaptive Signal Fusion System` becomes `patent-adaptive-signal-fusion`.

Before creating anything, check whether Conda is available and whether the environment already exists:

```powershell
conda --version
conda env list
```

If a matching environment exists, reuse it. If not, ask for approval before creating it. Prefer project-appropriate runtime versions and dependency files:

```powershell
conda create -n patent-project-slug python=3.11
conda activate patent-project-slug
```

Install dependencies inside that Conda environment according to the project: `environment.yml`, `requirements.txt`, `pyproject.toml`, frontend package manager files, or patent-specific runtime needs. Save or update an environment/dependency record when practical:

- Prefer `environment.yml` for Conda-managed Python projects.
- Preserve or create `requirements.txt` when the project uses pip-only dependency capture.
- For mixed Python/frontend projects, document both Conda/Python dependencies and frontend package-manager dependencies.
- Record the exact commands and environment name in the final delivery.

## Installation Boundary

This skill is a workflow and dependency guide, not a universal package manager. It can guide Codex to remind users, inspect whether dependencies appear available, and attempt installation where the environment supports it.

Automatic installation depends on:

- The recipient's Codex version and plugin support.
- Filesystem and network permissions.
- Whether `skill-installer` is installed and callable.
- Whether the required MCP servers have an accessible installation source.
- Whether the user approves downloads, global skill writes, or MCP configuration changes.

If automatic installation is not possible, provide a clear missing-dependency list and continue only with user approval of the reduced capability.

## First-Run Checklist

Before reading patent documents or writing code:

1. Confirm a suitable `.docx` reader is enabled for DOCX work.
2. Confirm a suitable `.pdf` reader is enabled for PDF work.
3. Confirm `$figma-generate-design` is installed for GUI design.
4. Confirm `fetch` and `duckduckgo` are available if external lookup is needed.
5. Confirm the user's local Conda is available or ask whether to install/enable/use a fallback.
6. Derive and confirm the Conda environment name from the patent project.
7. Confirm the user has provided the patent documents, datasets, and project files.
8. Confirm any missing document-reading capabilities and ask whether to install, enable, or proceed with reduced confidence.
