#!/usr/bin/env python3
"""
Data Directory & Document Catalog Synchronizer for PRJ-001 Kenya Public Debt
Scans Data/ (Raw, Interim, Processed, Published) and Sources/Documents/ to build
a machine-readable catalog.json and verify all files.
"""

import os
import hashlib
import json
import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
DOCS_DIR = BASE_DIR / "Sources" / "Documents"
OUTPUT_JSON = DATA_DIR / "catalog.json"

def get_file_sha256(filepath: Path) -> str:
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def inspect_csv(filepath: Path):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        row_count = sum(1 for _ in reader)
    return header, row_count

def scan_catalog():
    catalog = {
        "project_id": "PRJ-001",
        "last_scanned": datetime.utcnow().isoformat() + "Z",
        "stages": {
            "raw": [],
            "interim": [],
            "processed": [],
            "published": [],
            "documents": []
        }
    }

    # Scan Data subdirectories
    subdirs = {
        "raw": DATA_DIR / "Raw",
        "interim": DATA_DIR / "Interim",
        "processed": DATA_DIR / "Processed",
        "published": DATA_DIR / "Published"
    }

    DATA_EXTENSIONS = {".csv", ".tsv", ".xlsx", ".xls", ".parquet", ".json", ".zip", ".tar.gz", ".pdf"}

    for stage, path in subdirs.items():
        if not path.exists():
            continue
        for p in sorted(path.rglob("*")):
            if p.is_file() and not p.name.startswith(".") and p.suffix.lower() in DATA_EXTENSIONS and p.name != "catalog.json":
                rel_path = p.relative_to(BASE_DIR).as_posix()
                item = {
                    "filename": p.name,
                    "relative_path": rel_path,
                    "format": p.suffix.lstrip(".").upper(),
                    "size_bytes": p.stat().st_size,
                    "sha256": get_file_sha256(p),
                    "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat()
                }
                if p.suffix.lower() == ".csv":
                    try:
                        header, rows = inspect_csv(p)
                        item["columns"] = header
                        item["row_count"] = rows
                    except Exception:
                        pass
                catalog["stages"][stage].append(item)

    # Scan Sources/Documents
    if DOCS_DIR.exists():
        for p in sorted(DOCS_DIR.rglob("*")):
            if p.is_file() and not p.name.startswith(".") and p.suffix.lower() in DATA_EXTENSIONS:
                rel_path = p.relative_to(BASE_DIR).as_posix()
                item = {
                    "filename": p.name,
                    "relative_path": rel_path,
                    "format": p.suffix.lstrip(".").upper(),
                    "size_bytes": p.stat().st_size,
                    "sha256": get_file_sha256(p),
                    "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat()
                }
                catalog["stages"]["documents"].append(item)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)

    total_files = sum(len(items) for items in catalog["stages"].values())
    print(f"[OK] Scanned {total_files} files across Data/ and Sources/Documents/")
    print(f"[OK] Catalog written to: {OUTPUT_JSON}")

if __name__ == "__main__":
    scan_catalog()
