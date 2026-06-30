#!/usr/bin/env python3
"""
generate_readme.py — Builds the root README.md from data/categories/*.json.

This is the single source of truth pipeline: edit a category's JSON file,
re-run this script, and README.md (plus data/all_entries.json, used by the
search site) regenerate automatically. Never hand-edit README.md directly —
it will be overwritten.

Usage:
    python3 scripts/generate_readme.py
"""
import json
import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_DIR = ROOT / "data" / "categories"
README_PATH = ROOT / "README.md"
ALL_ENTRIES_PATH = ROOT / "data" / "all_entries.json"

PRICING_BADGES = {
    "free": "🟢 Free",
    "freemium": "🔵 Freemium",
    "free-trial": "🟡 Free Trial",
    "open-source": "🟣 Open Source",
    "paid": "🔴 Paid",
}

TABLE_CATEGORIES = {
    "major-cloud-providers",
    "serverless-functions",
    "databases",
    "static-hosting-cdn"
}

HEADER = """\
# Free (and Paid) Developer Resources

🚀 The ultimate curated directory of developer tools, APIs, and cloud services. 
Discover the best free tiers and compare paid alternatives for your next project.

This repo features structured machine-readable data (`data/categories/*.json`),
per-entry pricing model tags, paid-plan starting prices, "last verified" dates,
and a searchable static site.

**Browse interactively:** open `site/index.html` in a browser, or see
[Quick Start](#quick-start) below to run it locally.

> ⚠️ Pricing and free-tier limits change often. Each entry has a `lastVerified`
> date — if it looks stale, please open an issue or PR with updated info.

## Legend

| Badge | Meaning |
|---|---|
| 🟢 Free | Entirely free product/service |
| 🔵 Freemium | Perpetual free tier + paid upgrade path |
| 🟡 Free Trial | Time-boxed trial only, no perpetual free tier |
| 🟣 Open Source | Free/self-hostable OSS, may offer a paid hosted option |
| 🔴 Paid | No meaningful free tier; included for comparison |

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/free-and-paid-dev-resources.git
cd free-and-paid-dev-resources
pip install -r scripts/requirements.txt

# Validate all category data against the schema
python3 scripts/validate.py

# Regenerate README.md and data/all_entries.json from the category JSON files
python3 scripts/generate_readme.py

# Open site/index.html in your browser for the searchable UI
```

## Table of Contents

"""

FOOTER_TEMPLATE = """
---

*Inspired by and modeled after [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev).*

> 🤖 **Automated Maintenance:** This repository is actively maintained. A GitHub Action automatically checks all links every 7 days and opens an issue if any tool's website goes offline.

## Contributing

This repo follows a **JSON-first** workflow:

1. Find (or create) the relevant file under `data/categories/`.
2. Add your entry following `data/schema.json` (see existing entries for the shape).
3. Run `python3 scripts/validate.py` — fix anything it flags.
4. Run `python3 scripts/generate_readme.py` to regenerate `README.md` and the site's data file.
5. Open a PR. CI will re-run both scripts automatically and fail if `README.md` is out of sync with the JSON.

**Entry criteria** (same spirit as the original free-for-dev list):
- Must be a hosted/SaaS-style offering OR a meaningfully free/open-source self-hosted tool.
- If it has a free tier, it must be genuinely useful at that tier (not a 7-day trial dressed up as "free"; trials should use `"pricingModel": "free-trial"`).
- Paid-only entries are welcome **only** as comparison anchors for a category (tag with `"pricingModel": "paid"`).
- Include real, current numbers in `freeTier` — "generous free tier" is not acceptable, "500MB storage, 2 projects" is.

See [`.github/pull_request_template.md`](.github/pull_request_template.md) for the PR checklist.

## License

[MIT](LICENSE) — data and code in this repository. Trademarks and product names belong to their respective owners.

---

*Generated on {generated_date} from {category_count} category files, {entry_count} entries.
Do not hand-edit this file — edit `data/categories/*.json` and run `scripts/generate_readme.py`.*
"""


def load_categories():
    categories = []
    for path in sorted(CATEGORIES_DIR.glob("*.json")):
        with open(path) as f:
            categories.append(json.load(f))
    # Sort categories alphabetically by display name, except keep
    # "Major Cloud Providers (Deep Dive)" pinned near the top like the
    # original repo does with its big cloud vendor section.
    def sort_key(c):
        if c["slug"] == "major-cloud-providers":
            return (0, c["category"])
        return (1, c["category"])
    categories.sort(key=sort_key)
    return categories


def render_entry(entry):
    badge = PRICING_BADGES.get(entry["pricingModel"], entry["pricingModel"])
    lines = [f"### [{entry['name']}]({entry['url']}) — {badge}", ""]
    lines.append(entry["summary"])
    lines.append("")
    lines.append(f"- **Free tier:** {entry['freeTier']}")
    if entry.get("paidFrom"):
        lines.append(f"- **Paid from:** {entry['paidFrom']}")
    if entry.get("alternativeTo"):
        lines.append(f"- **Often compared to:** {entry['alternativeTo']}")
    if entry.get("notes"):
        lines.append(f"- **Note:** {entry['notes']}")
    tags = entry.get("tags", [])
    if tags:
        tag_str = " ".join(f"`{t}`" for t in tags)
        lines.append(f"- **Tags:** {tag_str}")
    lines.append(f"- *Last verified: {entry['lastVerified']}*")
    lines.append("")
    return "\n".join(lines)


def render_category(cat):
    lines = [f"## {cat['category']}", "", cat["description"], ""]
    
    if cat["slug"] in TABLE_CATEGORIES:
        lines.append("| Provider / Tool | Badge | Free Tier | Summary |")
        lines.append("|---|---|---|---|")
        for entry in cat["entries"]:
            badge = PRICING_BADGES.get(entry["pricingModel"], entry["pricingModel"])
            # Remove newlines so table rows don't break
            free_tier = entry["freeTier"].replace("\n", " ").replace("|", "\\|")
            summary = entry["summary"].replace("\n", " ").replace("|", "\\|")
            lines.append(f"| [{entry['name']}]({entry['url']}) | {badge} | {free_tier} | {summary} |")
        lines.append("")
    else:
        for entry in cat["entries"]:
            lines.append(render_entry(entry))
            
    lines.append("[⬆️ Back to Top](#table-of-contents)")
    lines.append("")
    return "\n".join(lines)


def github_anchor(text):
    """Mimics GitHub's Markdown heading -> anchor slug algorithm:
    lowercase, strip punctuation (keep word chars/spaces/hyphens), spaces -> hyphens."""
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = s.replace(" ", "-")
    s = re.sub(r"-+", "-", s)
    return s


def render_toc(categories):
    lines = []
    for cat in categories:
        anchor = github_anchor(cat["category"])
        lines.append(f"- [{cat['category']}](#{anchor})")
    return "\n".join(lines)


def build_all_entries_index(categories):
    """Flatten all entries into a single JSON array for the search site,
    with category metadata attached to each entry."""
    flat = []
    for cat in categories:
        for entry in cat["entries"]:
            flat.append({
                **entry,
                "category": cat["category"],
                "categorySlug": cat["slug"],
            })
    return flat


def main():
    categories = load_categories()
    total_entries = sum(len(c["entries"]) for c in categories)

    body_parts = [HEADER]
    body_parts.append(render_toc(categories))
    body_parts.append("\n")
    for cat in categories:
        body_parts.append(render_category(cat))

    footer = FOOTER_TEMPLATE.format(
        generated_date=date.today().isoformat(),
        category_count=len(categories),
        entry_count=total_entries,
    )
    body_parts.append(footer)

    README_PATH.write_text("\n".join(body_parts))

    flat = build_all_entries_index(categories)
    ALL_ENTRIES_PATH.write_text(json.dumps(flat, indent=2))

    print(f"✅ Wrote {README_PATH.relative_to(ROOT)} ({len(categories)} categories, {total_entries} entries)")
    print(f"✅ Wrote {ALL_ENTRIES_PATH.relative_to(ROOT)} ({len(flat)} flattened entries)")


if __name__ == "__main__":
    main()
