# Deliverables Checklist

Use this checklist before marking a `doc-to-code` project complete. Every item should be present or explicitly marked not applicable with a reason.

## Required Final Artifacts

- Patent claim to code mapping table.
- Conda environment summary.
- Test sample directory.
- Reproducible run commands.
- GUI frontend start command.
- Screenshots, logs, output files, or data traces.
- Unresolved ambiguity list.

## Patent Claim to Code Mapping

Provide a table with:

| Claim/Requirement | Source Reference | Implementation Location | Test/Sample | Runtime Evidence | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

- Use claim numbers, page numbers, paragraph IDs, figure IDs, table IDs, or heading names.
- Link each implemented behavior to source files or modules.
- Include tests, fixtures, command logs, or output files for each covered claim element.
- Mark unsupported or ambiguous claim elements as blocked or out of scope.

## Conda Environment Summary

Include:

- Environment name.
- How the name was derived from the patent project.
- Python/runtime version.
- Dependency source files such as `environment.yml`, `requirements.txt`, `pyproject.toml`, `package.json`, or lockfiles.
- Commands used to create, activate, install, test, and run.
- Any fallback if Conda was unavailable.

## Test Sample Directory

Provide or identify a test/sample directory containing:

- Input samples.
- Expected outputs.
- Fixtures.
- Unit tests and integration tests.
- Reproducible demo data.

Label sample data clearly as user-provided, patent-provided, generated, synthetic, or demo.

## Required Commands

Document commands for:

- Activating the Conda environment.
- Installing dependencies.
- Running unit and integration tests.
- Running reproducible sample executions.
- Starting backend services, if any.
- Starting the GUI frontend.
- Capturing or regenerating evidence artifacts.

## Evidence Files

Collect or identify:

- Test reports.
- Command logs.
- Runtime logs.
- Input/output bundles.
- Data traces.
- Generated visualizations.
- GUI screenshots or browser screenshots that show the running implementation.

Screenshots support the demonstration, but proof claims must be grounded in code, tests, logs, and data evidence.

## Unresolved Ambiguities

List each unresolved issue with:

- Source location.
- Ambiguous text or missing material.
- Possible interpretations.
- Implementation decision taken, if any.
- User confirmation status.
- Risk if left unresolved.
