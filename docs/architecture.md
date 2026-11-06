# Architecture overview

The private project has a local Python + SQLite application for writable content, owner approval, audit logs and append-only New sections. Its source and database integrity checks compare immutable starting material to pinned SHA-256 fingerprints.

This public showcase is intentionally separate: HTML, CSS and vanilla JavaScript render a fictional JSON dataset. A browser-side integrity page recomputes the dataset SHA-256 and compares it with a manifest. GitHub Pages can host this static read-only demonstration, but it cannot run the private Python/SQLite application or provide multi-user writes.
