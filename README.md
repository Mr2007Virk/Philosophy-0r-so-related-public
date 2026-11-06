# Philosophy Archive — Public Project Showcase

A public portfolio demonstration of an evidence-aware, append-only archive concept.

**This is a separate public showcase, not the private working archive.** It contains fictional demonstration records only. It does not include private philosophical reflections, original conversation exports, the SQLite database, owner PINs, or the working source library.

## What the project demonstrates

- A searchable, structured archive interface.
- Stable record identifiers and source labels.
- Preservation of original statements rather than silent rewriting.
- Conflict records that retain both sides and request an owner decision.
- Append-only, owner-approved updates.
- SHA-256 integrity checking against a separately stored manifest.
- A separation between a private working dataset and a public read-only showcase.

## Run locally

Open `index.html` in a browser for the record viewer. For integrity verification, use a local static web server (for example, Python's `python -m http.server 8000`) and open `http://localhost:8000/integrity.html`; browser Web Crypto requires a secure context such as localhost or HTTPS.

## Publish with GitHub Pages

1. Create a separate **public** GitHub repository named `philosophy-archive-showcase`.
2. From this folder, run `PUBLISH_TO_GITHUB.bat` after creating the empty repository.
3. In repository Settings → Pages, deploy from branch `main`, folder `/ (root)`.
4. Wait for GitHub Pages to finish deployment. The public URL appears under Settings → Pages.

Do not copy the private working database or real project archive into this repository.

## Authorship and credits

This is a personal project conceived and directed by its owner. Software implementation and documentation were developed with AI assistance. The owner should review this wording and choose a licence before publication.

## Scope and limitations

This static site is read-only. It is not a shared live database and does not accept writes. The integrity demo detects changes to the demo data relative to the published manifest; it is not a cryptographic security boundary against an attacker who can change both files.
