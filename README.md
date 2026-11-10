# Philosophy Archive — Public Project Showcase

A public portfolio demonstration of an evidence-aware, append-only archive concept.

**This repository is the public portfolio showcase for the project owner’s work.** It is deliberately separate from the private working repository. It contains fictional demonstration records only; it does not publish the private SQLite database, original conversation exports, private philosophical reflections, owner PIN, or private source library.

## What the project demonstrates

- A searchable, structured archive interface.
- Stable record identifiers and source labels.
- Preservation of original statements rather than silent rewriting.
- Conflict records that retain both sides and request an owner decision.
- Append-only, owner-approved updates as a demonstrated workflow concept.
- SHA-256 integrity checking for the fictional demonstration dataset.
- A clear separation between a private working archive and a public, read-only showcase.

## View the project

- **GitHub repository:** https://github.com/Mr2007Virk/Philosophy-0r-so-related-public
- **Website:** use the GitHub Pages URL shown under this repository’s Settings → Pages. The repository’s Pages build and deployment workflow has completed successfully; check that page for the current live URL and deployment status.

## Run locally

Open `index.html` in a browser for the record viewer. For integrity verification, use a local static web server (for example, `python -m http.server 8000`) and open `http://localhost:8000/integrity.html`. Browser Web Crypto requires a secure context such as localhost or HTTPS.

## Maintaining this existing repository

This project already has its public repository: `Mr2007Virk/Philosophy-0r-so-related-public`. **Do not create another repository named `philosophy-archive-showcase`.**

For changes, work from a clone of this repository, keep the public dataset fictional, run `python scripts/check_publication.py`, and confirm the `Public showcase checks` GitHub Actions workflow passes before treating the change as published. GitHub Pages deploys from this repository; check Settings → Pages if the deployment source needs review.

Never copy the private working database, original source records, conversation exports, personal reflections, owner PIN, local backups, or credentials into this repository.

## Authorship and credits

The project concept, requirements, direction and ownership belong to the project owner. Software implementation and documentation were developed with AI assistance, under the project owner’s direction and review. The public sample records are fictional and are not quotations from the private archive or real conversations. See `PROJECT_CREDITS.md` for the detailed attribution statement.

## Scope and limitations

This static site is read-only. It is not a shared live database and does not accept writes. The integrity demo detects changes to the fictional demo data when the published manifest remains unchanged; it is not a cryptographic security boundary against an attacker who can change both files. The publication checker adds filename and text-pattern screening for common private materials and credential formats, but no automated scanner can guarantee detection of every form of personal information or secret. Human review remains required before publication.
