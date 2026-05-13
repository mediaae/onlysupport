# Traceability Standard

Maintain a traceability matrix before and during implementation.

Recommended columns:

| ID | Source | Patent Text Summary | Interpretation | Code Location | Test/Evidence | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1-S1 | Claim 1 / page 12 | Normalized technical summary | Exact implementation decision | path:line or module | test name / screenshot / log | planned/done/blocked | ambiguity or assumption |

Rules:

- One row per claim element, processing step, figure behavior, data input/output, or proof requirement.
- Use stable source references: claim number, page, paragraph, table, figure, heading, or comment ID.
- Never mark a row done until code and evidence both exist.
- If code intentionally deviates from a literal reading, record the reason and get user approval.
- If a document is inconsistent, preserve both readings and ask for a decision.

Implementation discipline:

- Name domain functions after the patent's technical terms when practical.
- Keep transformations auditable: input, intermediate state, output, validation, and failure mode.
- Add tests for boundary cases stated or implied by the patent.
- Avoid clever shortcuts that make the proof hard to inspect.
- Do not implement a core algorithm, rule, or technical claim that the patent documents do not describe unless the user explicitly authorizes it.
- Do not present inference as fact. Label each technical step as `document-explicit`, `user-specified`, or `engineering-glue`.
- Do not claim coverage of all patent claims unless every covered claim element has a traceability row with code and test evidence.
- Keep ordinary engineering glue separate from patented behavior so reviewers can distinguish implementation support from claimed invention logic.

Review discipline:

- Search for implemented behavior with no traceability row.
- Search for traceability rows with no code or no test.
- Confirm the GUI displays the mechanism and runtime results, while proof remains grounded in code, tests, logs, data traces, and traceability evidence.
- Confirm sample data is labeled as sample/demo unless supplied by the patent materials.
