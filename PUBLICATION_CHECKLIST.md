# Public showcase release and privacy checklist

Status checked against the public repository on 11 November 2026. Re-run the checks before every future publication.

## Verified in the current public repository

- [x] The repository is public and is the intended personal-account showcase: `Mr2007Virk/Philosophy-0r-so-related-public`.
- [x] The tracked file tree contains the static showcase and demo materials; no SQLite database, owner PIN file, private source snapshot, original conversation export, local backup, or credential file was found by the audit.
- [x] The demonstration dataset is marked `fictional_demo_only`; its entries use `DEMO-` record and source IDs.
- [x] The website describes itself as a static, read-only demonstration and distinguishes itself from the private working archive.
- [x] The public showcase CI check passed on the currently inspected commit.
- [x] The GitHub Pages build and deployment workflow completed successfully on 6 November 2026.

## Required before the next publication

- [ ] Run `python scripts/check_publication.py` after replacing this checklist and the checker; confirm it passes in the repository root.
- [ ] Confirm the `Public showcase checks` workflow passes for the new commit.
- [ ] Review the rendered GitHub Pages website and confirm that its links and text are correct.
- [ ] Review `PROJECT_CREDITS.md` and confirm that the attribution accurately reflects the owner’s contribution and AI assistance.
- [ ] Make a deliberate licence decision. No open-source licence is currently selected.

## Permanent publication boundary

Never publish the private SQLite database, owner PIN, credentials, original conversation exports, private source snapshots, private archive records, personal philosophical reflections, local backups, or private working-repository contents. Keep only fictional sample records and generic system documentation in this public repository.
