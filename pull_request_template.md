## What does this PR add or change?

<!-- One sentence: e.g. "Adds Neon (serverless Postgres) to Databases category." -->

## Checklist

- [ ] I added/edited an entry in the correct file under `data/categories/*.json` (not in `README.md` directly)
- [ ] The entry follows the shape defined in `data/schema.json`
- [ ] `freeTier` contains **specific numbers** (storage, requests/month, users, etc.), not vague marketing language
- [ ] `pricingModel` is accurate: use `free-trial` (not `freemium`) if there is no perpetual free tier
- [ ] `url` points to the official site (not an affiliate/referral link)
- [ ] `lastVerified` is set to today's date (`YYYY-MM-DD`)
- [ ] I ran `python3 scripts/validate.py` and it passed
- [ ] I ran `python3 scripts/generate_readme.py` and committed the resulting changes to `README.md` and `data/all_entries.json`
- [ ] This service is genuinely useful to software engineers / DevOps / indie builders (in scope for this list)

## Why does this belong here?

<!-- Briefly: what makes this worth including? Especially important for paid-only entries (must serve as a useful comparison anchor). -->
