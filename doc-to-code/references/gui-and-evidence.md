# GUI and Proof Evidence Guide

Use `$figma-generate-design` after the requirements and traceability matrix are stable. A GUI-style frontend demonstration interface is required, not optional.

## GUI Goals

The interface is a distinctive presentation and interaction layer. It must help reviewers understand the implemented invention, but it is not the primary patent proof material. The proof material is the code, test samples, runtime outputs, logs, data traces, and traceability matrix.

- Show the patented process, not just generic CRUD screens.
- Make inputs, intermediate processing, outputs, and validation visible.
- Use terminology from the patent documents where it helps reviewers connect UI to claims.
- Provide data displays: tables, timelines, charts, state diagrams, comparison panels, logs, or metric cards as appropriate.
- Run against real implementation paths, fixtures, or reproducible samples rather than static mockups alone.
- Preserve a distinctive visual identity. Avoid generic dashboards, stock hero pages, and decorative layouts unrelated to the invention.

## Design Process

1. Summarize the invention mechanism and the implemented code/test proof path.
2. Identify primary users and reviewer needs.
3. Ask `$figma-generate-design` to produce a domain-specific GUI concept from the mechanism, data states, and reviewer understanding goals.
4. Translate the design into the project's frontend framework using existing UI patterns when present.
5. Wire the frontend to real code outputs, deterministic fixtures, or reproducible sample runs.
6. Verify responsive layout, data readability, and GUI execution with screenshots or browser tests.

## Frontend Stack Selection

Choose the frontend stack conservatively:

- Reuse the existing frontend framework if the project already has one.
- Use React/Vite for a new web demonstration when no frontend exists and the project has no stronger local convention.
- Use the project language's native GUI stack only when it better fits the patent demonstration, runtime constraints, or existing code.
- Keep the frontend small enough to be reviewed, tested, and run by a recipient.
- Do not deliver only Figma assets, screenshots, or static mockups. The GUI must be executable and connected to implementation outputs or reproducible fixtures.

## Evidence Artifacts

Prepare artifacts that can support patent demonstration:

- Traceability matrix.
- Implemented source code mapped to claim elements.
- Test samples, fixtures, and expected outputs.
- Test report, command log, runtime log, or reproducible execution transcript.
- Sample input/output bundles.
- Generated data traces and visualizations from real code execution.
- Screenshots only as supporting material that shows the running implementation or data display.
- Short implementation note explaining where each claim element appears in code.

Do not overclaim. If the prototype demonstrates only selected claims or selected embodiments, state that precisely.
