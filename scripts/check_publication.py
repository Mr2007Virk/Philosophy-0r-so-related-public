#!/usr/bin/env python3
"""Validate that the public showcase contains only fictional demo material.

This is a guardrail, not a guarantee that all personal information or secrets
can be detected. Human review remains required before publishing changes.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "index.html",
    "integrity.html",
    "data/demo-archive.json",
    "data/integrity-manifest.json",
    "docs/privacy-boundary.md",
    "docs/architecture.md",
    "PROJECT_CREDITS.md",
)

FORBIDDEN_SUFFIXES = {
    ".sqlite", ".sqlite3", ".db", ".pem", ".key", ".p12", ".pfx",
    ".sql", ".dump", ".bak", ".backup", ".old", ".orig",
}
FORBIDDEN_NAMES = {
    ".env", "owner_pin.txt", "credentials.json", "secrets.json",
    "id_rsa", "id_ed25519", "philosophy_archive.sqlite3",
    "philosophy_books_verbatim_v3.json",
}
FORBIDDEN_PRIVATE_DIRS = {
    "archive_application", "project_record", "project_materials",
    "conversation_exports_not_loaded", "current_source_snapshots",
    "historical_reference", "owner_provided_source",
    "private_working_archive", "private_source_snapshots",
}

SECRET_PATTERNS = (
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Stripe live secret", re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b")),
    ("OpenAI-style API key", re.compile(r"\bsk-[A-Za-z0-9_-]{32,}\b")),
    (
        "credential assignment",
        re.compile(
            r"\b(?:api[_ -]?key|access[_ -]?token|client[_ -]?secret|secret[_ -]?key|password|passwd)\b"
            r"\s*[:=]\s*[\"']?([A-Za-z0-9_./+=-]{16,})",
            re.IGNORECASE,
        ),
    ),
)
PRIVATE_KEY_MARKER = re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def scan_paths(errors: list[str]) -> tuple[int, int]:
    scanned = 0
    skipped_binary = 0
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.is_symlink():
            fail(f"Symbolic link must be reviewed manually: {path.relative_to(ROOT)}", errors)
            continue
        if not path.is_file():
            continue

        rel = path.relative_to(ROOT)
        name = path.name.lower()
        parts = {part.lower() for part in rel.parts[:-1]}
        if name in FORBIDDEN_NAMES:
            fail(f"Forbidden private/credential filename: {rel}", errors)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            fail(f"Forbidden database, backup, or key file type: {rel}", errors)
        if name.startswith(".env."):
            fail(f"Environment file must not be published: {rel}", errors)
        private_dirs = parts & FORBIDDEN_PRIVATE_DIRS
        if private_dirs:
            fail(f"Private archive directory found in public tree: {rel}", errors)

        # Scan bytes as UTF-8 with invalid sequences ignored. This still catches
        # ASCII credential patterns inside many non-text files; binary content
        # is counted separately so the report does not imply full binary review.
        raw = path.read_bytes()
        scanned += 1
        if b"\x00" in raw:
            skipped_binary += 1
        text = raw.decode("utf-8", errors="ignore")
        if PRIVATE_KEY_MARKER.search(text):
            fail(f"Private-key block detected in: {rel}", errors)
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"Possible {label} detected in: {rel} (value withheld)", errors)
    return scanned, skipped_binary


def main() -> int:
    errors: list[str] = []
    for item in REQUIRED_FILES:
        if not (ROOT / item).is_file():
            fail(f"Required showcase file missing: {item}", errors)

    manifest_path = ROOT / "data" / "integrity-manifest.json"
    data_path = ROOT / "data" / "demo-archive.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        data_bytes = data_path.read_bytes()
        actual = hashlib.sha256(data_bytes).hexdigest()
        if actual != manifest.get("sha256"):
            fail("Demo dataset fingerprint does not match the integrity manifest", errors)
        if manifest.get("file") != "demo-archive.json" or manifest.get("algorithm") != "SHA-256":
            fail("Integrity manifest must identify demo-archive.json and SHA-256", errors)
        data = json.loads(data_bytes.decode("utf-8"))
        if data.get("dataset_type") != "fictional_demo_only":
            fail("Dataset is not marked fictional_demo_only", errors)
        records = data.get("records")
        if not isinstance(records, list) or not records:
            fail("Demonstration dataset must contain a non-empty records list", errors)
        else:
            for index, record in enumerate(records, 1):
                if not isinstance(record, dict):
                    fail(f"Demo record {index} is not an object", errors)
                    continue
                if not str(record.get("id", "")).startswith("DEMO-"):
                    fail(f"Demo record {index} has a non-demo identifier", errors)
                if not str(record.get("source_id", "")).startswith("DEMO-"):
                    fail(f"Demo record {index} has a non-demo source identifier", errors)
                if "Fictional demo entry" not in str(record.get("author_label", "")):
                    fail(f"Demo record {index} is missing its fictional author label", errors)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"Could not validate demonstration data/manifest: {exc.__class__.__name__}", errors)

    # Ensure the public-facing text keeps the live/private boundary explicit.
    try:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        for phrase in ("fictional demonstration records only", "separate from the private working repository", "static site is read-only"):
            if phrase not in readme:
                fail(f"README is missing required privacy/scope statement: {phrase}", errors)
    except OSError:
        fail("README.md could not be read", errors)

    scanned, skipped_binary = scan_paths(errors)
    if errors:
        print("FAIL: public showcase publication checks did not pass")
        for error in errors:
            print(f" - {error}")
        print(f"Files inspected: {scanned}; binary files with limited content inspection: {skipped_binary}")
        return 1

    print("PASS: fictional dataset, SHA-256 manifest, required privacy statements, forbidden paths and common credential patterns verified.")
    print(f"Files inspected: {scanned}; binary files with limited content inspection: {skipped_binary}")
    print("Limitation: pattern screening cannot guarantee detection of every secret or personal detail; human review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
