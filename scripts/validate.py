#!/usr/bin/env python3
"""
validate.py — Validates every data/categories/*.json file against data/schema.json
and runs a handful of extra sanity checks (valid URLs, unique slugs, valid dates,
no duplicate entry names within a category).

Usage:
    python3 scripts/validate.py
Exit code 0 = all good, 1 = at least one error found.
"""
import json
import sys
import re
from pathlib import Path
from datetime import datetime

try:
    from jsonschema import validate, ValidationError
except ImportError:
    print("Missing dependency. Install with: pip install jsonschema --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "data" / "schema.json"
CATEGORIES_DIR = ROOT / "data" / "categories"

URL_RE = re.compile(r"^https?://")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_PRICING_MODELS = {"free", "freemium", "free-trial", "open-source", "paid"}


def load_schema():
    with open(SCHEMA_PATH) as f:
        return json.load(f)


def main():
    schema = load_schema()
    errors = []
    seen_slugs = {}
    total_entries = 0

    files = sorted(CATEGORIES_DIR.glob("*.json"))
    if not files:
        print(f"No category files found in {CATEGORIES_DIR}")
        sys.exit(1)

    for path in files:
        try:
            with open(path) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"[{path.name}] Invalid JSON: {e}")
            continue

        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            errors.append(f"[{path.name}] Schema error: {e.message} (path: {list(e.path)})")
            continue

        slug = data.get("slug")
        if slug in seen_slugs:
            errors.append(f"[{path.name}] Duplicate slug '{slug}' also used in {seen_slugs[slug]}")
        else:
            seen_slugs[slug] = path.name

        entry_names = set()
        for entry in data.get("entries", []):
            total_entries += 1
            name = entry.get("name", "<unnamed>")

            if name in entry_names:
                errors.append(f"[{path.name}] Duplicate entry name '{name}' within category")
            entry_names.add(name)

            url = entry.get("url", "")
            if not URL_RE.match(url):
                errors.append(f"[{path.name}] Entry '{name}' has invalid URL: {url}")

            pricing = entry.get("pricingModel", "")
            if pricing not in VALID_PRICING_MODELS:
                errors.append(f"[{path.name}] Entry '{name}' has invalid pricingModel: {pricing}")

            last_verified = entry.get("lastVerified", "")
            if not DATE_RE.match(last_verified):
                errors.append(f"[{path.name}] Entry '{name}' has invalid lastVerified date: {last_verified}")
            else:
                try:
                    datetime.strptime(last_verified, "%Y-%m-%d")
                except ValueError:
                    errors.append(f"[{path.name}] Entry '{name}' has unparseable date: {last_verified}")

            if pricing == "paid" and entry.get("freeTier", "").strip().lower() not in ("n/a", "none"):
                # Not a hard error, just a style nudge — paid entries should say N/A for freeTier.
                pass

    print(f"Checked {len(files)} category files, {total_entries} total entries.")

    if errors:
        print(f"\n❌ {len(errors)} issue(s) found:\n")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("✅ All category files passed validation.")
        sys.exit(0)


if __name__ == "__main__":
    main()
