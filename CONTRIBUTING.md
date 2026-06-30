# Contributing

Thanks for considering a contribution! This project follows a **JSON-first** workflow —
`README.md` is a *generated* file, not something you edit by hand.

## How content is structured

```
data/
  schema.json              # JSON Schema all category files must satisfy
  categories/
    source-code-hosting.json
    ci-cd.json
    ...                    # one file per category
  all_entries.json          # auto-generated flat index used by site/, do not hand-edit
README.md                   # auto-generated from data/categories/*.json, do not hand-edit
scripts/
  validate.py                # validates all category files against the schema
  generate_readme.py         # regenerates README.md + data/all_entries.json
site/
  index.html                  # searchable static site, reads data/all_entries.json
```

## Adding a new entry to an existing category

1. Open the relevant file under `data/categories/`.
2. Add an object to its `entries` array. Required fields:
   - `name`, `url`, `pricingModel`, `summary`, `freeTier`, `tags`, `lastVerified`
   - Optional: `paidFrom`, `notes`, `alternativeTo`
3. `pricingModel` must be one of: `free`, `freemium`, `free-trial`, `open-source`, `paid`.
4. `freeTier` should state **concrete numbers** — quotas, storage, request limits, seat counts.
   Avoid vague phrases like "generous free tier."
5. Set `lastVerified` to today's date in `YYYY-MM-DD` format — this is what you personally checked, not when the product launched.

## Adding a brand-new category

1. Create a new file under `data/categories/your-category-slug.json`.
2. Follow the shape in `data/schema.json` — `category`, `slug`, `description`, and an `entries` array.
3. Pick a `slug` that doesn't collide with an existing one (the validator will catch this).

## Before opening a PR

```bash
pip install -r scripts/requirements.txt
python3 scripts/validate.py          # must pass with no errors
python3 scripts/generate_readme.py   # regenerates README.md and data/all_entries.json
git add -A
git commit -m "Add <ServiceName> to <Category>"
```

CI re-runs both scripts on every PR and will fail the build if `README.md` or
`data/all_entries.json` don't match what the category JSON files would generate —
so always run `generate_readme.py` locally and commit the output.

## Removing or correcting an entry

Free tiers shrink, companies get acquired, free trials get rebranded as the
only option. If you notice an entry is stale or wrong:

- Update the JSON in place and bump `lastVerified`.
- If the product/free-tier no longer exists, delete the entry entirely rather
  than marking it `paid` with apologetic notes.
- For pricing changes, just update `freeTier` / `paidFrom` and the date — no
  need to explain the history in `notes` unless it's a notable gotcha.

## Style notes

- One sentence to three sentences for `summary` — what the product does, not why it's great.
- `notes` is for **gotchas only**: credit card required for free tier, regional
  restrictions, free tier recently changed, etc. Leave it out entirely if there's nothing notable.
- Tags are lowercase, hyphenated, and should help someone filter/search (e.g. `postgres`, `self-hosted`, `vector-db`).
