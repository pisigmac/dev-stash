# Free (and Paid) Developer Resources

A curated, structured catalog of SaaS, PaaS, IaaS, APIs, and developer utilities —
covering both free tiers and notable paid alternatives — for software engineers,
DevOps practitioners, and indie builders.

Inspired by and modeled after [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev),
this repo extends the format with structured machine-readable data
(`data/categories/*.json`), per-entry pricing model tags, paid-plan starting
prices, "last verified" dates, and a searchable static site.

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


- [Major Cloud Providers (Deep Dive)](#major-cloud-providers-deep-dive)
- [AI, LLMs & ML Platforms](#ai-llms-ml-platforms)
- [API Gateways, Docs & Developer Experience](#api-gateways-docs-developer-experience)
- [APIs & Data Services](#apis-data-services)
- [Authentication & Identity](#authentication-identity)
- [CI/CD & Build Automation](#cicd-build-automation)
- [Cloud Compute, PaaS & App Hosting](#cloud-compute-paas-app-hosting)
- [Cloud IDEs & Dev Environments](#cloud-ides-dev-environments)
- [Code Quality, Review & Static Analysis](#code-quality-review-static-analysis)
- [Containers, Kubernetes & Registries](#containers-kubernetes-registries)
- [Customer Support & Helpdesk](#customer-support-helpdesk)
- [Databases (SQL, NoSQL, Vector)](#databases-sql-nosql-vector)
- [Design, Prototyping & UI Assets](#design-prototyping-ui-assets)
- [Domains, DNS & SSL/TLS](#domains-dns-ssltls)
- [Email, SMS & Transactional Messaging](#email-sms-transactional-messaging)
- [Feature Flags & Experimentation](#feature-flags-experimentation)
- [Forms, Surveys & Customer Feedback](#forms-surveys-customer-feedback)
- [Headless CMS & Content Management](#headless-cms-content-management)
- [Learning, Education & Student Developer Packs](#learning-education-student-developer-packs)
- [Low-Code, No-Code & Automation](#low-code-no-code-automation)
- [Monitoring, Logging & Observability](#monitoring-logging-observability)
- [Object & File Storage](#object-file-storage)
- [Payments & Billing](#payments-billing)
- [Project Management & Team Collaboration](#project-management-team-collaboration)
- [Search & Analytics](#search-analytics)
- [Secrets Management & Security](#secrets-management-security)
- [Serverless Functions & Backend-as-a-Service](#serverless-functions-backend-as-a-service)
- [Source Code Hosting](#source-code-hosting)
- [Static Site Hosting & CDN](#static-site-hosting-cdn)
- [Testing & QA](#testing-qa)
- [Video, Voice & Real-Time Communication](#video-voice-real-time-communication)


## Major Cloud Providers (Deep Dive)

Expanded detail on the 'big' multi-service clouds, since each spans compute, storage, databases, and more under one free-tier umbrella.

### [AWS Free Tier — Compute & Storage Bundle](https://aws.amazon.com/free) — 🔵 Freemium

AWS bundles dozens of always-free and 12-month-free service allowances across EC2, S3, RDS, Lambda, and DynamoDB.

- **Free tier:** 750 EC2 hrs/month (12mo), 5GB S3 (12mo), 750 RDS hrs/month (12mo), 1M Lambda requests/month (always-free), 25GB DynamoDB (always-free).
- **Note:** Distinguish 'always free' services from '12 months free' services — many people get billed unexpectedly after month 12.
- **Tags:** `cloud` `multi-service` `always-free` `12-month-free`
- *Last verified: 2026-06-01*

### [Google Cloud Free Program](https://cloud.google.com/free) — 🔵 Freemium

Combines an always-free tier (small but permanent) with a one-time $300 trial credit for 90 days.

- **Free tier:** 1 e2-micro VM, 5GB Cloud Storage, 2M Cloud Functions invocations/month always-free; $300 credit for new accounts.
- **Tags:** `cloud` `multi-service` `always-free` `trial-credit`
- *Last verified: 2026-06-01*

### [Microsoft Azure Free Account](https://azure.microsoft.com/free) — 🔵 Freemium

Mix of always-free service quotas (25+ services) plus a $200 credit for the first 30 days.

- **Free tier:** 1 B1S VM (12mo), 1M Azure Functions executions/month (always-free), 5GB Blob + 5GB File storage (12mo), $200 trial credit.
- **Tags:** `cloud` `multi-service` `always-free` `trial-credit`
- *Last verified: 2026-06-01*

### [Oracle Cloud Always Free](https://www.oracle.com/cloud/free) — 🔵 Freemium

OCI's always-free tier is unusually generous and has no 12-month expiration on its core compute offer.

- **Free tier:** 4 Arm Ampere A1 cores + 24GB RAM (split across up to 4 VMs), 2 AMD E2.1.Micro VMs, 200GB block storage, 10TB egress/month, all permanently free.
- **Note:** Often cited as the best free always-on compute available from any major cloud provider.
- **Tags:** `cloud` `arm` `always-free` `no-expiration`
- *Last verified: 2026-06-01*

### [IBM Cloud Lite](https://www.ibm.com/cloud/free) — 🔵 Freemium

IBM's Lite plans apply across dozens of services (Kubernetes, Cloud Functions, Watson AI, Cloudant) with no time limit, just usage caps.

- **Free tier:** Lite tier limits vary per service but never expire by time, only by usage quota.
- **Tags:** `cloud` `multi-service` `lite-plan` `watson-ai`
- *Last verified: 2026-05-01*

### [Cloudflare Free Plan](https://www.cloudflare.com/plans) — 🔵 Freemium

Cloudflare's free plan spans DNS, CDN, DDoS protection, SSL, Workers, Pages, and R2 storage under one umbrella.

- **Free tier:** Unlimited DNS-protected domains, free SSL, 100k Workers requests/day, 500 Pages builds/month, 10GB R2 storage/month.
- **Tags:** `cloud` `multi-service` `cdn` `edge` `dns`
- *Last verified: 2026-06-01*

### [Zoho Suite (Catalyst, Mail, Assist, Sprints)](https://www.zoho.com) — 🔵 Freemium

Zoho's developer-relevant free tiers span PaaS (Catalyst), email, remote support (Assist), and project tracking (Sprints).

- **Free tier:** Catalyst PaaS generous free tier; Mail free for 5 users (5GB/user); Assist free for 1 concurrent session; Sprints free for 5 users/5 projects/500MB.
- **Tags:** `cloud` `multi-service` `paas` `email`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## AI, LLMs & ML Platforms

LLM API providers, AI coding assistants, ML experiment tracking, and notebook/GPU compute for machine learning.

### [Anthropic Claude API](https://www.anthropic.com/api) — 🔵 Freemium

Access to the Claude family of models for chat, coding, and agentic tasks via API, console, and SDKs.

- **Free tier:** New accounts get limited starter credits; no perpetual free API tier — usage billed per-token after credits.
- **Paid from:** Pay-as-you-go per-token pricing varies by model tier.
- **Note:** Free chat usage is available at claude.ai separately from the metered developer API.
- **Tags:** `llm` `api` `ai`
- *Last verified: 2026-06-01*

### [OpenAI API](https://platform.openai.com) — 🔵 Freemium

API access to GPT and other OpenAI models for text, code, image, and audio generation.

- **Free tier:** New accounts may receive limited trial credits; ongoing use is metered, pay-as-you-go.
- **Paid from:** Pay-as-you-go per-token pricing varies by model.
- **Tags:** `llm` `api` `ai`
- *Last verified: 2026-06-01*

### [Google AI Studio / Gemini API](https://ai.google.dev) — 🔵 Freemium

Free and paid access to Google's Gemini models for text, vision, and multimodal tasks via API.

- **Free tier:** Free tier with rate-limited requests per minute/day for several Gemini model variants.
- **Paid from:** Pay-as-you-go tier removes rate limits, billed per-token.
- **Tags:** `llm` `api` `multimodal` `google`
- *Last verified: 2026-06-01*

### [Groq](https://groq.com) — 🔵 Freemium

Ultra-low-latency LLM inference API running open models (Llama, Mixtral, etc.) on custom LPU hardware.

- **Free tier:** Free developer tier with generous rate limits for popular open models.
- **Paid from:** Pay-as-you-go pricing for higher throughput.
- **Tags:** `llm` `api` `inference` `open-models`
- *Last verified: 2026-06-01*

### [Hugging Face](https://huggingface.co) — 🔵 Freemium

Hub for open-source models, datasets, and Spaces (hosted demos), plus Inference API and AutoTrain.

- **Free tier:** Unlimited public model/dataset hosting, free CPU Spaces, free-tier Inference API rate limits.
- **Paid from:** PRO plan from $9/month; dedicated Inference Endpoints billed hourly.
- **Tags:** `llm` `open-source` `model-hub` `inference`
- *Last verified: 2026-06-01*

### [OpenRouter](https://openrouter.ai) — 🔵 Freemium

Unified API gateway routing requests across dozens of LLM providers, with several free model endpoints.

- **Free tier:** Several models offered completely free with rate limits; pay-as-you-go for premium models.
- **Tags:** `llm` `api` `gateway` `model-routing`
- *Last verified: 2026-06-01*

### [Google Colab](https://colab.research.google.com) — 🔵 Freemium

Free hosted Jupyter notebooks with GPU/TPU access, popular for ML experimentation and education.

- **Free tier:** Free tier with rotating GPU access (subject to availability and usage limits).
- **Paid from:** Colab Pro from ~$9.99/month for more compute and priority GPUs.
- **Tags:** `notebooks` `gpu` `jupyter` `ml`
- *Last verified: 2026-05-01*

### [Kaggle Notebooks](https://www.kaggle.com) — 🟢 Free

Free GPU/TPU-enabled notebooks plus datasets and ML competitions, run by Google.

- **Free tier:** 30 GPU hours/week free, 20GB disk, free TPU quota.
- **Tags:** `notebooks` `gpu` `datasets` `competitions`
- *Last verified: 2026-05-01*

### [Weights & Biases](https://wandb.ai) — 🔵 Freemium

Experiment tracking, model registry, and collaboration platform for ML teams.

- **Free tier:** Free for personal/academic use with limited tracked hours and storage.
- **Paid from:** Pro plan billed per seat.
- **Tags:** `mlops` `experiment-tracking` `model-registry`
- *Last verified: 2026-04-01*

### [Comet ML](https://www.comet.com) — 🔵 Freemium

MLOps platform for experiment tracking, model production monitoring, and full data lineage.

- **Free tier:** Free tier for individuals with limited tracked experiments.
- **Paid from:** Teams plan billed per seat.
- **Tags:** `mlops` `experiment-tracking` `monitoring`
- *Last verified: 2026-04-01*

### [GitHub Copilot](https://github.com/features/copilot) — 🔵 Freemium

AI pair-programmer offering inline code completion and chat, integrated into popular IDEs.

- **Free tier:** Free tier with limited monthly completions/chat requests; free for students and verified open-source maintainers.
- **Paid from:** Individual plan from $10/month.
- **Tags:** `ai-coding` `code-completion` `ide-integration`
- *Last verified: 2026-06-01*

### [Codeium / Windsurf](https://windsurf.com) — 🔵 Freemium

AI coding assistant with inline completions and an agentic IDE (Windsurf), focused on low-latency suggestions.

- **Free tier:** Free tier with unlimited inline completions and limited premium model credits.
- **Paid from:** Pro plan from $15/month.
- **Tags:** `ai-coding` `ide` `code-completion`
- *Last verified: 2026-05-01*

### [Cursor](https://www.cursor.com) — 🔵 Freemium

AI-native code editor (VS Code fork) with deep multi-file context, chat, and agent modes.

- **Free tier:** Free tier (Hobby) includes limited number of premium AI requests/month.
- **Paid from:** Pro plan from $20/month.
- **Tags:** `ai-coding` `ide` `agentic`
- *Last verified: 2026-06-01*

### [v0.dev](https://v0.dev) — 🔵 Freemium

Vercel's AI tool generating copy-paste-ready React UI code using shadcn/ui and Tailwind from text prompts.

- **Free tier:** Starting credits plus a small monthly free credit allowance.
- **Paid from:** Premium plan from $20/month for more generation credits.
- **Tags:** `ai-coding` `ui-generation` `react`
- *Last verified: 2026-05-01*

### [Replicate](https://replicate.com) — 🔵 Freemium

Run open-source ML models (image, audio, video, LLM) via API without managing infrastructure.

- **Free tier:** Small free credit for new accounts; ongoing usage is metered per-second of compute.
- **Tags:** `ml-inference` `api` `open-source-models`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## API Gateways, Docs & Developer Experience

API gateway/management platforms, API documentation tools, and SDK/client generation utilities.

### [Kong](https://konghq.com) — 🔵 Freemium

API gateway and marketplace for managing public and private APIs, with a strong open-source core.

- **Free tier:** Kong Gateway (OSS) is fully free; Konnect cloud has a free tier for small workloads.
- **Paid from:** Konnect plans billed on usage beyond free tier.
- **Tags:** `api-gateway` `open-source` `api-management`
- *Last verified: 2026-04-01*

### [Apidog](https://apidog.com) — 🔵 Freemium

All-in-one API design, documentation, mocking, and testing tool with key authentication, rate limiting, and monetization features.

- **Free tier:** Free plan: up to 10 projects, 1M monthly requests, 10GB egress.
- **Paid from:** Paid plans add team collaboration and higher quotas.
- **Tags:** `api-design` `api-docs` `mocking` `monetization`
- *Last verified: 2026-05-01*

### [ReadMe](https://readme.com) — 🔵 Freemium

Beautiful, interactive API documentation hubs with built-in API explorer and changelogs.

- **Free tier:** Free plan available for open-source projects.
- **Paid from:** Startup plan from $99/month.
- **Tags:** `api-docs` `developer-portal`
- *Last verified: 2026-03-01*

### [Swagger / SwaggerHub](https://swagger.io) — 🔵 Freemium

OpenAPI tooling for designing, documenting, and testing REST APIs, including the widely used Swagger UI.

- **Free tier:** Swagger Editor/UI tools fully free and open source; SwaggerHub has a free tier for individuals.
- **Paid from:** Team plan billed per user.
- **Tags:** `openapi` `api-docs` `open-source`
- *Last verified: 2026-04-01*

### [Stoplight](https://stoplight.io) — 🔵 Freemium

API design platform with visual OpenAPI editing, mocking, and style-guide linting.

- **Free tier:** Free tier for individuals with limited projects.
- **Paid from:** Professional plan billed per user.
- **Tags:** `api-design` `openapi` `mocking`
- *Last verified: 2026-03-01*

### [Mintlify](https://mintlify.com) — 🔵 Freemium

Modern documentation platform with a beautiful default theme, built for developer-facing docs sites.

- **Free tier:** Free tier for open-source/community projects.
- **Paid from:** Starter plan billed monthly.
- **Tags:** `documentation` `developer-docs`
- *Last verified: 2026-04-01*

### [Docusaurus](https://docusaurus.io) — 🟣 Open Source

Meta's open-source static site generator purpose-built for documentation sites, with versioning and i18n support.

- **Free tier:** Completely free, open source; deploy anywhere (e.g., GitHub Pages, Vercel, Netlify free tiers).
- **Tags:** `documentation` `static-site-generator` `open-source`
- *Last verified: 2026-05-01*

### [newreleases.io](https://newreleases.io) — 🔵 Freemium

Tracks new releases across GitHub, GitLab, PyPI, npm, RubyGems, NuGet, Cargo, Docker Hub, and more, with webhook/chat alerts.

- **Free tier:** Free tier with limited tracked projects and notification channels.
- **Paid from:** Premium plan billed monthly for more tracked projects.
- **Tags:** `release-tracking` `notifications` `webhooks`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## APIs & Data Services

Third-party APIs providing geolocation, weather, financial, automotive, and other structured data.

### [IPinfo](https://ipinfo.io) — 🔵 Freemium

Fast, accurate IP geolocation and company/carrier data API.

- **Free tier:** Up to 100,000 requests/month free.
- **Paid from:** Basic plan from $49/month.
- **Tags:** `ip-geolocation` `api`
- *Last verified: 2026-04-01*

### [IP Geolocation API (ipgeolocation.io)](https://ipgeolocation.io) — 🔵 Freemium

IP geolocation API with timezone, currency, and astronomy data add-ons.

- **Free tier:** 30,000 requests/month (1,000/day) forever free.
- **Paid from:** Paid plans from $15/month.
- **Tags:** `ip-geolocation` `api`
- *Last verified: 2026-03-01*

### [OpenWeatherMap](https://openweathermap.org/api) — 🔵 Freemium

Current weather, forecasts, and historical weather data API covering global locations.

- **Free tier:** 1,000 calls/day free on the current weather and forecast endpoints.
- **Paid from:** Startup plan from $40/month.
- **Tags:** `weather` `api`
- *Last verified: 2026-04-01*

### [REST Countries](https://restcountries.com) — 🟢 Free

Free REST API for retrieving country information — names, capitals, currencies, flags, and more.

- **Free tier:** Free, unlimited use, no API key required.
- **Tags:** `geography` `reference-data` `api`
- *Last verified: 2026-02-01*

### [Country State City API](https://countrystatecity.in) — 🔵 Freemium

Hierarchical location data API: countries, states/provinces, cities, and postal codes.

- **Free tier:** 100 requests/day free.
- **Paid from:** Paid plans for higher volume.
- **Tags:** `geography` `reference-data` `api`
- *Last verified: 2026-03-01*

### [CarAPI.dev](https://carapi.app) — 🔵 Freemium

Automotive data API covering VIN decoding, vehicle specs, valuation, and stolen vehicle checks.

- **Free tier:** 100 requests/month across all endpoints free.
- **Paid from:** Paid plans from $19/month.
- **Tags:** `automotive` `vin-decoding` `api`
- *Last verified: 2026-04-01*

### [Alpha Vantage](https://www.alphavantage.co) — 🔵 Freemium

Stock, forex, and crypto market data API with technical indicators.

- **Free tier:** 25 requests/day free.
- **Paid from:** Premium plans from $49.99/month.
- **Tags:** `finance` `stock-market` `api`
- *Last verified: 2026-04-01*

### [Exchange Rate API](https://www.exchangerate-api.com) — 🔵 Freemium

Currency conversion and exchange rate data API.

- **Free tier:** 1,500 requests/month free.
- **Paid from:** Paid plans from $9.99/month.
- **Tags:** `finance` `currency` `api`
- *Last verified: 2026-03-01*

### [NewsAPI](https://newsapi.org) — 🔵 Freemium

Search and retrieve news articles from thousands of sources worldwide.

- **Free tier:** Developer plan free for non-commercial use, 100 requests/day.
- **Paid from:** Business plan from $449/month for commercial use.
- **Tags:** `news` `content-aggregation` `api`
- *Last verified: 2026-03-01*

### [FullContact](https://www.fullcontact.com) — 🔵 Freemium

Identity resolution API enriching contact records with social profiles and demographic data.

- **Free tier:** 500 free Person API matches/month.
- **Paid from:** Paid plans billed per match.
- **Tags:** `identity-resolution` `enrichment` `api`
- *Last verified: 2026-02-01*

### [Cloudmersive](https://cloudmersive.com) — 🔵 Freemium

Utility API platform covering document conversion, virus scanning, image processing, and validation.

- **Free tier:** 600 calls/month free, North America region only on free tier.
- **Paid from:** Paid plans from $19/month.
- **Tags:** `document-conversion` `virus-scanning` `utility-api`
- *Last verified: 2026-03-01*

### [Conversion Tools](https://www.conversiontools.io) — 🔵 Freemium

Online file converter for documents, images, video, audio, and eBooks, with a REST API and SDKs.

- **Free tier:** 20MB file size limit, 30/day and 300/month conversions free.
- **Paid from:** Paid plans support files up to 50GB.
- **Tags:** `file-conversion` `api`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Authentication & Identity

User authentication, identity management, and authorization services (login, SSO, MFA, OAuth).

### [Auth0](https://auth0.com) — 🔵 Freemium

Identity platform handling login, SSO, MFA, and social auth via SDKs and a hosted login flow.

- **Free tier:** Free tier for up to 25,000 monthly active users (consumer use case).
- **Paid from:** Essentials plan from $35/month.
- **Tags:** `auth` `sso` `mfa` `identity`
- *Last verified: 2026-06-01*

### [Clerk](https://clerk.com) — 🔵 Freemium

Drop-in authentication and user management with pre-built UI components for React/Next.js and others.

- **Free tier:** 10,000 monthly active users free.
- **Paid from:** Pro plan from $25/month + per-MAU pricing beyond included users.
- **Tags:** `auth` `user-management` `react` `nextjs`
- *Last verified: 2026-06-01*

### [Firebase Auth](https://firebase.google.com/products/auth) — 🔵 Freemium

Google's identity platform supporting email/password, phone, and social logins (Google, GitHub, Facebook, etc.).

- **Free tier:** Unlimited free for most providers; phone auth free up to 10k verifications/month.
- **Tags:** `auth` `google` `phone-auth` `social-login`
- *Last verified: 2026-05-01*

### [Supabase Auth](https://supabase.com/auth) — 🔵 Freemium

Open-source auth built on PostgreSQL with row-level security, included as part of the Supabase platform.

- **Free tier:** 50,000 monthly active users free on Supabase's free project tier.
- **Tags:** `auth` `postgres` `open-source` `rls`
- *Last verified: 2026-05-01*

### [WorkOS](https://workos.com) — 🔵 Freemium

Enterprise-ready auth APIs (SSO, SCIM, audit logs) designed for B2B SaaS selling into large organizations.

- **Free tier:** Free up to 1 million monthly active users for core user management.
- **Paid from:** SSO/SCIM modules billed per connection.
- **Tags:** `sso` `scim` `enterprise` `b2b`
- *Last verified: 2026-05-01*

### [Okta / Auth0 by Okta](https://www.okta.com) — 🔵 Freemium

Enterprise identity and access management platform for workforce and customer identity.

- **Free tier:** Developer Edition free for testing, limited MAUs.
- **Paid from:** Workforce Identity plans billed per user.
- **Tags:** `sso` `identity` `enterprise`
- *Last verified: 2026-04-01*

### [Duo Security](https://duo.com) — 🔵 Freemium

Two-factor authentication (2FA/MFA) for apps, VPNs, and infrastructure logins.

- **Free tier:** Free for up to 10 users, all auth methods, hardware token support included.
- **Paid from:** Essentials plan billed per user.
- **Tags:** `mfa` `2fa` `vpn`
- *Last verified: 2026-03-01*

### [Foxpass](https://www.foxpass.com) — 🔵 Freemium

Hosted LDAP and RADIUS for per-user logins across servers, VPNs, and Wi-Fi networks.

- **Free tier:** Free tier for small teams (limited users).
- **Paid from:** Paid plans billed per user.
- **Tags:** `ldap` `radius` `network-auth`
- *Last verified: 2026-03-01*

### [Ory](https://www.ory.sh) — 🔵 Freemium

Open-source identity infrastructure (Kratos, Hydra, Keto) with a managed cloud option for auth, OAuth2, and permissions.

- **Free tier:** Free tier with limited monthly active users on Ory Network; self-hosted OSS is free.
- **Paid from:** Production plan billed per MAU beyond free quota.
- **Tags:** `open-source` `oauth2` `permissions` `self-hosted`
- *Last verified: 2026-04-01*

### [Stytch](https://stytch.com) — 🔵 Freemium

API-first authentication platform specializing in passwordless, passkeys, and fraud/risk signals.

- **Free tier:** Free tier covering limited monthly active users.
- **Paid from:** Growth plan billed per MAU beyond free quota.
- **Tags:** `passwordless` `passkeys` `fraud-detection`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## CI/CD & Build Automation

Continuous integration and continuous delivery platforms for building, testing, and deploying code automatically.

### [GitHub Actions](https://github.com/features/actions) — 🔵 Freemium

Workflow automation built into GitHub for CI/CD, testing, and release pipelines, with a huge marketplace of reusable actions.

- **Free tier:** 2,000 minutes/month for private repos (Linux), unlimited minutes for public repos.
- **Paid from:** Additional minutes billed per-minute beyond included quota.
- **Tags:** `ci-cd` `automation` `github`
- *Last verified: 2026-06-01*

### [CircleCI](https://circleci.com) — 🔵 Freemium

Cloud CI/CD platform with Docker-first pipelines, parallelism, and orbs (reusable config packages).

- **Free tier:** 6,000 build minutes/month free, up to 30 concurrent jobs on free plan.
- **Paid from:** Performance plan from $15/month.
- **Tags:** `ci-cd` `docker` `automation`
- *Last verified: 2026-06-01*

### [Travis CI](https://www.travis-ci.com) — 🔵 Freemium

One of the original hosted CI services, deeply integrated with GitHub for open-source and private builds.

- **Free tier:** Free tier available for open-source projects.
- **Paid from:** Paid plans from $69/month for private repos.
- **Tags:** `ci-cd` `open-source`
- *Last verified: 2026-03-10*

### [AppVeyor](https://www.appveyor.com) — 🔵 Freemium

CI/CD focused on Windows and .NET projects, also supports Linux and macOS builds.

- **Free tier:** Unlimited build minutes for one concurrent job on public/open-source repos.
- **Paid from:** Paid plans from $39/month for private projects.
- **Tags:** `ci-cd` `windows` `dotnet`
- *Last verified: 2026-03-10*

### [Codemagic](https://codemagic.io) — 🔵 Freemium

CI/CD purpose-built for mobile apps (Flutter, React Native, iOS, Android) with code signing automation.

- **Free tier:** 500 free build minutes/month.
- **Paid from:** Pay-as-you-go from $0.038/build minute beyond free quota.
- **Tags:** `ci-cd` `mobile` `flutter` `react-native`
- *Last verified: 2026-05-01*

### [Buildkite](https://buildkite.com) — 🔵 Freemium

Hybrid CI/CD platform where you run your own build agents while Buildkite manages orchestration and UI.

- **Free tier:** Free for unlimited users on the open-source/small-team plan with limited pipeline minutes.
- **Paid from:** Paid plans scale with pipeline runs.
- **Tags:** `ci-cd` `self-hosted-agents` `orchestration`
- *Last verified: 2026-03-10*

### [Codefresh](https://codefresh.io) — 🔵 Freemium

Kubernetes-native CI/CD and GitOps platform with built-in Docker registry and pipeline visualization.

- **Free tier:** Free tier includes limited builds/month for individuals.
- **Paid from:** Team plans from $0.75 per build credit.
- **Tags:** `ci-cd` `kubernetes` `gitops` `docker`
- *Last verified: 2026-03-10*

### [Semaphore CI](https://semaphoreci.com) — 🔵 Freemium

Fast, container-based CI/CD with generous free compute credits and a focus on pipeline speed.

- **Free tier:** Free tier with monthly compute credits (no credit card required to start).
- **Paid from:** Startup plan from $18/month.
- **Tags:** `ci-cd` `containers` `fast-builds`
- *Last verified: 2026-03-10*

### [Drone CI](https://www.drone.io) — 🟣 Open Source

Container-native, self-hostable CI/CD engine configured entirely with YAML pipelines.

- **Free tier:** Fully free and open source when self-hosted.
- **Tags:** `ci-cd` `self-hosted` `containers` `open-source`
- *Last verified: 2026-03-10*

### [Jenkins](https://www.jenkins.io) — 🟣 Open Source

The most widely deployed self-hosted automation server, with an enormous plugin ecosystem covering nearly any CI/CD need.

- **Free tier:** Completely free, open source, self-hosted.
- **Tags:** `ci-cd` `self-hosted` `plugins` `open-source`
- *Last verified: 2026-03-10*

### [Render (Background Workers/CI)](https://render.com) — 🔵 Freemium

Deploys directly from Git with built-in CI, primarily known as a PaaS but covers full build-test-deploy pipelines.

- **Free tier:** Free web services with auto-deploy from Git (services sleep after inactivity).
- **Paid from:** Starter plans from $7/month per service.
- **Tags:** `ci-cd` `paas` `deploy`
- *Last verified: 2026-06-01*

### [CodSpeed](https://codspeed.io) — 🔵 Freemium

Performance regression tracking for CI pipelines, benchmarking code on every PR with consistent metrics.

- **Free tier:** Free forever for open-source projects.
- **Tags:** `ci-cd` `performance` `benchmarking`
- *Last verified: 2026-04-10*

[⬆️ Back to Top](#table-of-contents)

## Cloud Compute, PaaS & App Hosting

Virtual machines, container platforms, and platform-as-a-service offerings for running applications in the cloud.

### [Amazon Web Services (AWS)](https://aws.amazon.com/free) — 🔵 Freemium

The largest cloud provider, with hundreds of services spanning compute, storage, databases, ML, and networking.

- **Free tier:** 750 hrs/month t2.micro/t3.micro EC2 (12 months), 5GB S3 standard storage, 1M Lambda requests/month always-free, 25GB DynamoDB always-free.
- **Paid from:** Pay-as-you-go beyond free tier limits.
- **Often compared to:** Google Cloud, Azure
- **Note:** Free tier mixes 12-month time-limited offers with always-free tiers; check expiration per service.
- **Tags:** `cloud` `iaas` `compute` `serverless`
- *Last verified: 2026-06-01*

### [Google Cloud Platform](https://cloud.google.com/free) — 🔵 Freemium

Google's cloud platform with strong Kubernetes (GKE), BigQuery, and AI/ML offerings, plus a generous always-free tier.

- **Free tier:** 1 non-preemptible e2-micro VM/month, 5GB Cloud Storage, 2M Cloud Functions invocations/month, $300 in trial credits for 90 days.
- **Paid from:** Pay-as-you-go beyond free tier limits.
- **Tags:** `cloud` `iaas` `kubernetes` `bigquery`
- *Last verified: 2026-06-01*

### [Microsoft Azure](https://azure.microsoft.com/free) — 🔵 Freemium

Microsoft's cloud platform, strong on enterprise integration, .NET tooling, and hybrid cloud.

- **Free tier:** 1 B1S Linux/Windows VM (12 months), 1M Azure Functions requests/month always-free, 5GB Blob Storage, $200 credit for 30 days.
- **Paid from:** Pay-as-you-go beyond free tier limits.
- **Tags:** `cloud` `iaas` `dotnet` `enterprise`
- *Last verified: 2026-06-01*

### [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/free) — 🔵 Freemium

Notable for the most generous always-free compute tier among major clouds, including ARM-based instances.

- **Free tier:** 4 Arm-based Ampere A1 cores with 24GB RAM always-free, 2 AMD micro VMs, 200GB block storage, 10TB egress/month.
- **Note:** The Ampere A1 always-free allocation is the largest free compute offer of any major cloud as of 2026.
- **Tags:** `cloud` `iaas` `arm` `always-free`
- *Last verified: 2026-06-01*

### [IBM Cloud](https://www.ibm.com/cloud/free) — 🔵 Freemium

IBM's cloud platform with Lite-tier services spanning Kubernetes, Cloud Functions, Watson AI, and databases.

- **Free tier:** Lite plans free indefinitely for many services (limited compute/storage quotas, no time limit).
- **Tags:** `cloud` `iaas` `watson-ai` `lite-plan`
- *Last verified: 2026-05-01*

### [Cloudflare Workers / Pages](https://workers.cloudflare.com) — 🔵 Freemium

Edge compute (Workers) and static site/full-stack hosting (Pages) running on Cloudflare's global network.

- **Free tier:** 100,000 Workers requests/day, Pages: 500 builds/month, 100 custom domains, unlimited bandwidth.
- **Paid from:** Workers Paid plan from $5/month.
- **Tags:** `edge-compute` `serverless` `static-hosting` `cdn`
- *Last verified: 2026-06-01*

### [Render](https://render.com) — 🔵 Freemium

Modern Heroku-style PaaS for web services, static sites, cron jobs, and managed Postgres/Redis.

- **Free tier:** Free web services (spin down after 15 min idle), free static site hosting with unlimited bandwidth.
- **Paid from:** Starter instances from $7/month.
- **Tags:** `paas` `static-hosting` `managed-db`
- *Last verified: 2026-06-01*

### [Fly.io](https://fly.io) — 🔵 Freemium

Deploys Docker containers close to users across a global network of regions, with a focus on low-latency apps.

- **Free tier:** Small allowance of free compute/storage; exact quotas vary, check current pricing page.
- **Paid from:** Usage-based billing beyond free allowance.
- **Note:** Free tier terms have changed multiple times; always confirm on the pricing page before relying on it.
- **Tags:** `paas` `docker` `edge` `global-deploy`
- *Last verified: 2026-05-01*

### [Railway](https://railway.com) — 🔵 Freemium

Developer-friendly PaaS for deploying apps, databases, and cron jobs directly from GitHub with minimal config.

- **Free tier:** Trial credit for new accounts; ongoing usage-based Hobby plan with small monthly included usage.
- **Paid from:** Hobby plan from $5/month base + usage.
- **Tags:** `paas` `deploy` `databases`
- *Last verified: 2026-05-01*

### [Vercel](https://vercel.com) — 🔵 Freemium

Frontend cloud built for Next.js and other frameworks, with instant global deploys and edge functions.

- **Free tier:** Hobby plan free for personal projects: 100GB bandwidth/month, serverless + edge functions included.
- **Paid from:** Pro plan from $20/month/user.
- **Tags:** `frontend` `jamstack` `nextjs` `serverless`
- *Last verified: 2026-06-01*

### [Netlify](https://www.netlify.com) — 🔵 Freemium

JAMstack hosting platform with CI/CD, serverless functions, and form handling built in.

- **Free tier:** 100GB bandwidth/month, 300 build minutes/month, 125k serverless function invocations/month.
- **Paid from:** Pro plan from $19/member/month.
- **Tags:** `frontend` `jamstack` `static-hosting` `serverless`
- *Last verified: 2026-06-01*

### [Heroku](https://www.heroku.com) — 🔴 Paid

One of the original app PaaS platforms; removed its free tier in 2022, now entry-level paid only.

- **Free tier:** N/A — no perpetual free tier since November 2022.
- **Paid from:** Eco dynos from $5/month.
- **Note:** Included for comparison/migration context; previously the most common 'free dev hosting' reference.
- **Tags:** `paas` `deploy` `legacy`
- *Last verified: 2026-04-01*

### [Koyeb](https://www.koyeb.com) — 🔵 Freemium

Serverless platform for deploying APIs, web apps, and databases across global regions with autoscaling.

- **Free tier:** Free tier includes limited compute (e.g., one small always-on service).
- **Paid from:** Usage-based pricing beyond free allotment.
- **Tags:** `paas` `serverless` `autoscaling`
- *Last verified: 2026-05-01*

### [PythonAnywhere](https://www.pythonanywhere.com) — 🔵 Freemium

Browser-based Python development and hosting environment with a built-in console, editor, and scheduler.

- **Free tier:** One free web app on a subdomain, limited CPU seconds/day, 512MB storage.
- **Paid from:** Hacker plan from $5/month.
- **Tags:** `python` `paas` `beginner-friendly`
- *Last verified: 2026-04-01*

### [Glitch](https://glitch.com) — 🔵 Freemium

In-browser collaborative coding and instant hosting, popular for prototypes, bots, and small Node/Python apps.

- **Free tier:** Free apps with limited always-on uptime, community remixing.
- **Paid from:** Pro plan adds boosted apps and custom domains.
- **Tags:** `prototyping` `browser-ide` `collaborative`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Cloud IDEs & Dev Environments

Browser-based and cloud-hosted development environments for coding without local setup.

### [GitHub Codespaces](https://github.com/features/codespaces) — 🔵 Freemium

Full VS Code-in-the-browser dev environments spun up directly from a GitHub repo, with devcontainer support.

- **Free tier:** 120 core-hours/month free for personal accounts.
- **Paid from:** Pay-as-you-go beyond free quota, billed per core-hour.
- **Tags:** `cloud-ide` `github` `devcontainers`
- *Last verified: 2026-06-01*

### [Gitpod](https://www.gitpod.io) — 🔵 Freemium

Ephemeral, automated cloud dev environments configured via a repo-committed config file.

- **Free tier:** 50 free hours/month on the free plan.
- **Paid from:** Pro plan billed per usage beyond free hours.
- **Tags:** `cloud-ide` `ephemeral-environments`
- *Last verified: 2026-05-01*

### [Replit](https://replit.com) — 🔵 Freemium

Browser-based IDE supporting 50+ languages with instant hosting, multiplayer editing, and an AI agent.

- **Free tier:** Free tier with limited compute and storage for public Repls.
- **Paid from:** Core plan from $25/month.
- **Tags:** `cloud-ide` `instant-hosting` `multiplayer`
- *Last verified: 2026-06-01*

### [CodeSandbox](https://codesandbox.io) — 🔵 Freemium

Instant web-based IDE and sandboxes for frontend prototyping, with live preview and npm support.

- **Free tier:** Free tier with limited private sandboxes and compute.
- **Paid from:** Pro plan from $9/month.
- **Tags:** `cloud-ide` `frontend-prototyping` `sandboxes`
- *Last verified: 2026-05-01*

### [StackBlitz](https://stackblitz.com) — 🔵 Freemium

WebContainers-powered IDE that runs Node.js entirely in-browser for near-instant project boot times.

- **Free tier:** Free for public projects with core editing features.
- **Paid from:** Pro plan from $20/month for private projects.
- **Tags:** `cloud-ide` `webcontainers` `instant-boot`
- *Last verified: 2026-05-01*

### [Google Cloud Shell](https://cloud.google.com/shell) — 🟢 Free

Free browser-based shell and code editor with pre-installed gcloud tooling, for managing GCP resources.

- **Free tier:** Free with weekly usage hour quota, no separate billing.
- **Tags:** `cloud-shell` `google-cloud` `free-compute`
- *Last verified: 2026-04-01*

### [AWS Cloud9](https://aws.amazon.com/cloud9) — 🔵 Freemium

Cloud IDE running on an EC2 instance or connected to existing infrastructure, integrated with AWS services.

- **Free tier:** No separate Cloud9 fee; billed only for underlying EC2 compute (eligible for AWS Free Tier EC2 hours).
- **Tags:** `cloud-ide` `aws` `ec2-backed`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Code Quality, Review & Static Analysis

Tools for automated code review, static analysis, linting, and code coverage tracking.

### [CodeRabbit](https://coderabbit.ai) — 🔵 Freemium

AI-powered code review tool integrating with GitHub/GitLab to leave contextual review comments on PRs automatically.

- **Free tier:** 200 files/hour, 3 reviews/hour, 50 conversations/hour; free forever for open source.
- **Paid from:** Pro plan from $24/developer/month.
- **Tags:** `code-review` `ai` `github` `gitlab`
- *Last verified: 2026-06-01*

### [Codacy](https://www.codacy.com) — 🔵 Freemium

Automated code review covering style, security, duplication, and complexity across 40+ languages.

- **Free tier:** Free for unlimited public and private repositories on the open-source plan.
- **Paid from:** Pro plan from $18/month.
- **Tags:** `code-review` `static-analysis` `security`
- *Last verified: 2026-05-01*

### [CodeFactor](https://www.codefactor.io) — 🔵 Freemium

Automated code review for Git repos with quality grading and trend tracking.

- **Free tier:** Unlimited users and public repos free, plus one private repo.
- **Paid from:** Pro plan from $4.99/month.
- **Tags:** `code-review` `static-analysis`
- *Last verified: 2026-04-01*

### [Codecov](https://codecov.io) — 🔵 Freemium

Code coverage reporting and visualization, integrates with CI to show coverage diffs on PRs.

- **Free tier:** Free for open source; one free private repo.
- **Paid from:** Pro plan billed per seat.
- **Tags:** `code-coverage` `testing` `ci-integration`
- *Last verified: 2026-04-01*

### [SonarCloud](https://sonarcloud.io) — 🔵 Freemium

Cloud-hosted static analysis for bugs, vulnerabilities, and code smells, from the makers of SonarQube.

- **Free tier:** Free for public/open-source projects with unlimited lines of code.
- **Paid from:** Private repo pricing based on lines of code analyzed.
- **Tags:** `static-analysis` `security` `code-smells`
- *Last verified: 2026-05-01*

### [DeepSource](https://deepsource.com) — 🔵 Freemium

Continuous static analysis covering bug risk, performance, security, and anti-patterns, with autofix suggestions.

- **Free tier:** Free for open-source repositories.
- **Paid from:** Team plan from $8/contributor/month.
- **Tags:** `static-analysis` `autofix` `security`
- *Last verified: 2026-04-01*

### [Snyk](https://snyk.io) — 🔵 Freemium

Developer-first security platform scanning for vulnerabilities in code, open-source dependencies, containers, and IaC.

- **Free tier:** Free tier with limited monthly tests across code/open-source/container scanning.
- **Paid from:** Team plan from $25/product/month.
- **Tags:** `security` `dependency-scanning` `sast` `container-scanning`
- *Last verified: 2026-06-01*

### [Dependabot](https://github.com/dependabot) — 🟢 Free

Automated dependency update PRs built into GitHub, covering most major package ecosystems.

- **Free tier:** Completely free for all public and private GitHub repos.
- **Tags:** `dependency-updates` `security` `automation`
- *Last verified: 2026-06-01*

### [Codeac.io](https://www.codeac.io) — 🔵 Freemium

Automated Infrastructure-as-Code review integrating with GitHub, Bitbucket, and self-hosted GitLab.

- **Free tier:** Free tier for small/open-source projects.
- **Paid from:** Paid plans scale with repo count.
- **Tags:** `iac` `terraform` `ansible` `kubernetes`
- *Last verified: 2026-03-01*

### [Better Code Hub](https://bettercodehub.com) — 🔵 Freemium

Automated code maintainability checks based on the Software Improvement Group's 10 guidelines.

- **Free tier:** Free for public GitHub repositories.
- **Tags:** `maintainability` `static-analysis`
- *Last verified: 2026-02-01*

[⬆️ Back to Top](#table-of-contents)

## Containers, Kubernetes & Registries

Container image registries, managed Kubernetes, and container orchestration tooling.

### [Docker Hub](https://hub.docker.com) — 🔵 Freemium

The default public container registry, widely used to distribute and pull Docker images.

- **Free tier:** Unlimited public repos free; rate-limited anonymous/free-tier pulls.
- **Paid from:** Pro plan from $5/month for higher pull rate limits and private repos.
- **Tags:** `container-registry` `docker`
- *Last verified: 2026-05-01*

### [GitHub Container Registry (ghcr.io)](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) — 🔵 Freemium

Container registry built into GitHub Packages, tightly integrated with GitHub Actions for CI/CD publishing.

- **Free tier:** Free storage and bandwidth for public images.
- **Paid from:** Private image storage billed per GB beyond free GitHub plan quota.
- **Tags:** `container-registry` `github` `ci-cd`
- *Last verified: 2026-05-01*

### [Amazon ECR Public](https://gallery.ecr.aws) — 🔵 Freemium

AWS's public container registry gallery for sharing and discovering open-source container images.

- **Free tier:** Free storage and pulls for public images.
- **Paid from:** Private ECR billed per GB stored/transferred.
- **Tags:** `container-registry` `aws`
- *Last verified: 2026-04-01*

### [Quay.io](https://quay.io) — 🔵 Freemium

Red Hat's container registry with built-in vulnerability scanning and robot accounts for CI automation.

- **Free tier:** Free for public repositories with unlimited storage.
- **Paid from:** Paid plans add private repos and higher build concurrency.
- **Tags:** `container-registry` `vulnerability-scanning` `red-hat`
- *Last verified: 2026-03-01*

### [Civo](https://www.civo.com) — 🔵 Freemium

Fast-provisioning managed Kubernetes (k3s-based) cloud, known for sub-90-second cluster creation.

- **Free tier:** Free credits for new accounts; no perpetual free cluster.
- **Paid from:** Clusters billed from ~$5/month per node.
- **Tags:** `kubernetes` `managed-k8s` `fast-provisioning`
- *Last verified: 2026-04-01*

### [Oracle Container Engine for Kubernetes (OKE)](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes) — 🔵 Freemium

Managed Kubernetes service that runs on top of OCI's generous always-free compute tier.

- **Free tier:** Control plane free; worker nodes can run on OCI's always-free Ampere A1 compute.
- **Tags:** `kubernetes` `managed-k8s` `always-free-compute`
- *Last verified: 2026-04-01*

### [k3s](https://k3s.io) — 🟣 Open Source

Lightweight, certified Kubernetes distribution from Rancher, ideal for edge, IoT, and local dev clusters.

- **Free tier:** Completely free and open source, self-hosted.
- **Tags:** `kubernetes` `open-source` `lightweight` `edge`
- *Last verified: 2026-04-01*

### [Portainer](https://www.portainer.io) — 🔵 Freemium

Web UI for managing Docker, Docker Swarm, and Kubernetes environments without the raw CLI.

- **Free tier:** Community Edition free for up to 5 nodes (or 3 for Kubernetes).
- **Paid from:** Business Edition billed per node.
- **Tags:** `container-management` `kubernetes` `docker` `ui`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Customer Support & Helpdesk

Helpdesk, live chat, and customer support ticketing tools for product and engineering teams.

### [Crisp](https://crisp.chat) — 🔵 Freemium

Live chat, shared inbox, and basic CRM for small support teams.

- **Free tier:** Free plan for up to 2 seats with core chat features.
- **Paid from:** Pro plan from $25/month.
- **Tags:** `live-chat` `helpdesk` `small-teams`
- *Last verified: 2026-04-01*

### [Tawk.to](https://www.tawk.to) — 🟢 Free

Free live chat widget and ticketing system with unlimited agents and chat history.

- **Free tier:** 100% free for unlimited agents and chat volume.
- **Paid from:** Add-ons (e.g., remove branding, hire chat agents) are paid.
- **Tags:** `live-chat` `helpdesk` `free`
- *Last verified: 2026-04-01*

### [Chatwoot](https://www.chatwoot.com) — 🟣 Open Source

Open-source customer engagement platform (live chat, omnichannel inbox), self-hostable or managed cloud.

- **Free tier:** Self-hosted fully free; Cloud free tier for small teams.
- **Paid from:** Cloud Startup plan from $19/month.
- **Tags:** `live-chat` `open-source` `omnichannel`
- *Last verified: 2026-04-01*

### [Freshdesk](https://www.freshworks.com/freshdesk) — 🔵 Freemium

Helpdesk and ticketing system with automation, SLAs, and a knowledge base builder.

- **Free tier:** Free plan for up to 10 agents with core ticketing.
- **Paid from:** Growth plan from $15/agent/month.
- **Tags:** `helpdesk` `ticketing` `knowledge-base`
- *Last verified: 2026-04-01*

### [Zendesk](https://www.zendesk.com) — 🔴 Paid

Enterprise-grade customer service platform covering ticketing, chat, and a help center.

- **Free tier:** N/A — no perpetual free tier, trial only.
- **Paid from:** Support Team plan from $19/agent/month.
- **Tags:** `helpdesk` `enterprise` `ticketing`
- *Last verified: 2026-04-01*

### [Papercups](https://github.com/papercups-io/papercups) — 🟣 Open Source

Open-source live customer chat platform, an Intercom alternative you can self-host.

- **Free tier:** Self-hosted fully free.
- **Tags:** `live-chat` `open-source` `self-hosted`
- *Last verified: 2026-02-01*

[⬆️ Back to Top](#table-of-contents)

## Databases (SQL, NoSQL, Vector)

Managed database-as-a-service offerings across relational, document, key-value, graph, and vector databases.

### [Supabase](https://supabase.com) — 🔵 Freemium

Open-source Firebase alternative providing a managed Postgres database with auth, storage, realtime, and edge functions.

- **Free tier:** 2 free projects, 500MB database, 1GB file storage, 5GB bandwidth/month, projects pause after 1 week inactivity.
- **Paid from:** Pro plan from $25/month/project.
- **Tags:** `postgres` `backend-as-a-service` `auth` `realtime`
- *Last verified: 2026-06-01*

### [Neon](https://neon.com) — 🔵 Freemium

Serverless Postgres with branching (database copies for dev/test) and scale-to-zero compute.

- **Free tier:** 0.5GB storage, generous compute hours/month, unlimited branches on free tier.
- **Paid from:** Launch plan from $19/month.
- **Tags:** `postgres` `serverless` `branching`
- *Last verified: 2026-06-01*

### [PlanetScale](https://planetscale.com) — 🔵 Freemium

Serverless MySQL-compatible platform built on Vitess, with non-blocking schema migrations and branching workflows.

- **Free tier:** Hobby plan free with limited storage and row reads/writes per month.
- **Paid from:** Scaler plan from $39/month.
- **Tags:** `mysql` `vitess` `serverless` `branching`
- *Last verified: 2026-06-01*

### [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) — 🔵 Freemium

Fully managed MongoDB document database with a free shared-cluster tier that never expires.

- **Free tier:** M0 cluster: 512MB storage, shared RAM/vCPU, no time limit.
- **Paid from:** Dedicated clusters from ~$9/month (M2).
- **Tags:** `mongodb` `nosql` `document-db`
- *Last verified: 2026-06-01*

### [Firebase (Firestore/Realtime DB)](https://firebase.google.com/pricing) — 🔵 Freemium

Google's mobile/web app backend platform including Firestore NoSQL database, auth, hosting, and analytics.

- **Free tier:** Spark plan free: 1GB Firestore storage, 50k reads/20k writes per day.
- **Paid from:** Blaze plan is pay-as-you-go beyond Spark limits.
- **Tags:** `nosql` `backend-as-a-service` `mobile` `realtime`
- *Last verified: 2026-06-01*

### [Upstash](https://upstash.com) — 🔵 Freemium

Serverless Redis, Kafka, and vector database with per-request pricing ideal for spiky/serverless workloads.

- **Free tier:** 10,000 commands/day free on Redis, 10,000 vectors free on vector DB.
- **Paid from:** Pay-as-you-go beyond free request quota.
- **Tags:** `redis` `serverless` `kafka` `vector-db`
- *Last verified: 2026-06-01*

### [Redis Cloud](https://redis.io/cloud) — 🔵 Freemium

Official managed Redis offering with a permanently free small database tier.

- **Free tier:** 30MB free database, shared infrastructure, no time limit.
- **Paid from:** Flexible plans from ~$5/month for fixed dedicated.
- **Tags:** `redis` `caching` `in-memory`
- *Last verified: 2026-05-01*

### [CockroachDB Cloud](https://www.cockroachlabs.com/get-started-cockroachdb) — 🔵 Freemium

Distributed SQL database that's Postgres wire-compatible, designed for resilience and horizontal scale.

- **Free tier:** Free tier with 10GiB storage and 50M request units/month.
- **Paid from:** Standard plan billed on usage above free tier.
- **Tags:** `distributed-sql` `postgres-compatible` `horizontal-scale`
- *Last verified: 2026-05-01*

### [Turso](https://turso.tech) — 🔵 Freemium

Edge-replicated SQLite database (built on libSQL) for low-latency reads close to users.

- **Free tier:** 500 databases, 9GB total storage, 1B row reads/month on free tier.
- **Paid from:** Scaler plan from $29/month.
- **Tags:** `sqlite` `edge-db` `libsql`
- *Last verified: 2026-05-01*

### [Pinecone](https://www.pinecone.io) — 🔵 Freemium

Managed vector database purpose-built for similarity search and RAG/AI applications.

- **Free tier:** Starter tier free: 1 project, ~2GB storage (serverless), limited read/write units.
- **Paid from:** Standard plan billed on usage.
- **Tags:** `vector-db` `ai` `rag` `embeddings`
- *Last verified: 2026-05-01*

### [Weaviate Cloud](https://weaviate.io) — 🔵 Freemium

Open-source vector database with managed cloud hosting and hybrid (vector + keyword) search.

- **Free tier:** Sandbox cluster free for 14 days; open-source self-hosted version is free indefinitely.
- **Paid from:** Serverless cloud billed on usage.
- **Tags:** `vector-db` `open-source` `hybrid-search`
- *Last verified: 2026-05-01*

### [Astra DB (DataStax)](https://www.datastax.com/products/datastax-astra) — 🔵 Freemium

Managed Cassandra-based database with vector search support, built for high-scale NoSQL workloads.

- **Free tier:** 25M reads/writes and 25GB storage free per month, no expiry.
- **Paid from:** Pay-as-you-go beyond free monthly allowance.
- **Tags:** `cassandra` `nosql` `vector-search`
- *Last verified: 2026-04-01*

### [ElephantSQL (Postgres)](https://www.elephantsql.com) — 🔵 Freemium

Simple managed PostgreSQL hosting with a small permanently-free tier, good for quick prototypes.

- **Free tier:** 20MB storage, shared instance, no time limit.
- **Paid from:** Paid plans from ~$9/month.
- **Tags:** `postgres` `simple-hosting`
- *Last verified: 2026-03-01*

### [Xata](https://xata.io) — 🔵 Freemium

Serverless Postgres platform with built-in full-text search, file attachments, and branching.

- **Free tier:** Free tier with limited storage and request quotas for small projects.
- **Paid from:** Pro plan billed on usage.
- **Tags:** `postgres` `serverless` `full-text-search`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Design, Prototyping & UI Assets

UI/UX design tools, prototyping software, icon/illustration libraries, and design-to-code utilities.

### [Figma](https://www.figma.com) — 🔵 Freemium

Collaborative interface design tool with prototyping, dev handoff, and a huge community plugin ecosystem.

- **Free tier:** Free for up to 3 collaborative design files, unlimited personal files.
- **Paid from:** Professional plan from $12/editor/month.
- **Tags:** `ui-design` `prototyping` `collaboration`
- *Last verified: 2026-06-01*

### [Canva](https://www.canva.com) — 🔵 Freemium

Drag-and-drop design tool for social graphics, presentations, and marketing assets.

- **Free tier:** Free plan with thousands of templates and core editing tools.
- **Paid from:** Pro plan from $12.99/month.
- **Tags:** `graphic-design` `templates` `marketing`
- *Last verified: 2026-05-01*

### [Penpot](https://penpot.app) — 🟣 Open Source

Open-source design and prototyping platform, a self-hostable alternative to Figma built on open web standards (SVG).

- **Free tier:** Free cloud plan with generous limits; fully free self-hosted.
- **Tags:** `ui-design` `open-source` `self-hosted` `prototyping`
- *Last verified: 2026-05-01*

### [Storybook](https://storybook.js.org) — 🟣 Open Source

Open-source tool for building, documenting, and testing UI components in isolation.

- **Free tier:** Completely free and open source.
- **Tags:** `component-library` `open-source` `documentation`
- *Last verified: 2026-05-01*

### [unDraw](https://undraw.co) — 🟢 Free

Open-source illustration library with a consistent style, customizable colors, free for commercial use.

- **Free tier:** Unlimited free downloads, no attribution required.
- **Tags:** `illustrations` `open-source` `design-assets`
- *Last verified: 2026-03-01*

### [Heroicons](https://heroicons.com) — 🟢 Free

Free, MIT-licensed SVG icon set by the makers of Tailwind CSS, with solid and outline variants.

- **Free tier:** Free, unlimited, open source (MIT license).
- **Tags:** `icons` `open-source` `tailwind`
- *Last verified: 2026-03-01*

### [Lucide](https://lucide.dev) — 🟢 Free

Community-maintained fork of Feather Icons with a much larger, actively growing icon set.

- **Free tier:** Free, open source (ISC license), 1,500+ icons.
- **Tags:** `icons` `open-source`
- *Last verified: 2026-03-01*

### [Coolors](https://coolors.co) — 🔵 Freemium

Fast color palette generator with export to CSS, image extraction, and accessibility checks.

- **Free tier:** Free palette generation, export, and basic exploration tools.
- **Paid from:** Pro plan from $0.83/month (annual).
- **Tags:** `color-palette` `design-tools`
- *Last verified: 2026-02-01*

### [Maze](https://maze.co) — 🔵 Freemium

Rapid user testing and product research platform that connects to Figma prototypes.

- **Free tier:** Free plan with limited monthly tests/responses.
- **Paid from:** Starter plan from $99/month.
- **Tags:** `user-testing` `research` `figma-integration`
- *Last verified: 2026-03-01*

### [Excalidraw](https://excalidraw.com) — 🟢 Free

Virtual whiteboard for sketching diagrams with a hand-drawn aesthetic, open source and browser-based.

- **Free tier:** Free to use in-browser, no account required; open-source self-hosting also free.
- **Tags:** `whiteboard` `diagrams` `open-source`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Domains, DNS & SSL/TLS

Domain registration, DNS hosting, and SSL/TLS certificate issuance services.

### [Cloudflare DNS](https://www.cloudflare.com/dns) — 🟢 Free

Fast, free authoritative DNS hosting with built-in DDoS protection and analytics.

- **Free tier:** Unlimited domains on free DNS, free SSL/TLS, free DDoS protection.
- **Tags:** `dns` `ddos-protection` `ssl`
- *Last verified: 2026-05-01*

### [Let's Encrypt](https://letsencrypt.org) — 🟢 Free

Free, automated, open certificate authority issuing domain-validated TLS certificates, used by most of the web.

- **Free tier:** Completely free, unlimited certificates, automated renewal via ACME protocol.
- **Tags:** `ssl` `tls` `certificate-authority` `automation`
- *Last verified: 2026-05-01*

### [ZeroSSL](https://zerossl.com) — 🔵 Freemium

Alternative free SSL certificate provider with a web dashboard and ACME support.

- **Free tier:** Free 90-day certificates with manual or automated renewal.
- **Paid from:** Paid plans add longer validity and wildcard support.
- **Tags:** `ssl` `tls` `certificate-authority`
- *Last verified: 2026-04-01*

### [Cloudflare Registrar](https://www.cloudflare.com/products/registrar) — 🟢 Free

Domain registration at wholesale cost with no markup, bundled with Cloudflare's DNS and security features.

- **Free tier:** No markup on domain pricing (you pay registry cost only, no add-on fees).
- **Tags:** `domain-registration` `dns` `wholesale-pricing`
- *Last verified: 2026-04-01*

### [Namecheap](https://www.namecheap.com) — 🔵 Freemium

Popular domain registrar with free WHOIS privacy and DNS management included on most TLDs.

- **Free tier:** Free DNS management and WHOIS privacy guard with domain purchase.
- **Paid from:** Domain pricing varies by TLD.
- **Tags:** `domain-registration` `whois-privacy` `dns`
- *Last verified: 2026-03-01*

### [DuckDNS](https://www.duckdns.org) — 🟢 Free

Free dynamic DNS service for giving a home server or self-hosted project a stable subdomain.

- **Free tier:** Free subdomains under duckdns.org with dynamic IP updates.
- **Tags:** `dynamic-dns` `self-hosting` `home-server`
- *Last verified: 2026-03-01*

### [Freenom (historical)](https://www.freenom.com) — 🟢 Free

Historically offered free domains on select TLDs (.tk, .ml, .ga, .cf, .gq); service availability has fluctuated.

- **Free tier:** Previously free domains on certain ccTLDs; verify current registration status before relying on this.
- **Note:** Service availability and trustworthiness have been inconsistent; double-check current status before use.
- **Tags:** `domain-registration` `free-tld`
- *Last verified: 2026-01-15*

### [DNSimple](https://dnsimple.com) — 🔵 Freemium

DNS management and domain registration with a clean API, popular for automating DNS-as-code workflows.

- **Free tier:** 30-day free trial; no perpetual free tier for paid plans.
- **Paid from:** Personal plan from $5/month.
- **Tags:** `dns` `domain-registration` `dns-api`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Email, SMS & Transactional Messaging

Transactional email delivery, SMS/voice APIs, and push notification services for application messaging.

### [SendGrid](https://sendgrid.com) — 🔵 Freemium

Transactional and marketing email delivery API with templates, analytics, and deliverability tooling.

- **Free tier:** 100 emails/day free, forever.
- **Paid from:** Essentials plan from $19.95/month.
- **Tags:** `email` `transactional` `marketing-email`
- *Last verified: 2026-05-01*

### [Mailgun](https://www.mailgun.com) — 🔵 Freemium

Developer-focused email API for sending, receiving, validating, and tracking email at scale.

- **Free tier:** Free trial credits for new accounts; ongoing free tier limited to a small monthly send volume.
- **Paid from:** Foundation plan from $15/month.
- **Tags:** `email` `transactional` `api`
- *Last verified: 2026-05-01*

### [Resend](https://resend.com) — 🔵 Freemium

Modern transactional email API built with developer experience in mind, with React Email templating support.

- **Free tier:** 3,000 emails/month free, 1 domain.
- **Paid from:** Pro plan from $20/month.
- **Tags:** `email` `transactional` `react-email`
- *Last verified: 2026-06-01*

### [Postmark](https://postmarkapp.com) — 🔵 Freemium

Transactional email delivery focused on speed and deliverability, with detailed bounce/spam analytics.

- **Free tier:** 100 emails/month free trial-style tier.
- **Paid from:** Paid plans from $15/month for 10,000 emails.
- **Tags:** `email` `transactional` `deliverability`
- *Last verified: 2026-04-01*

### [Amazon SES](https://aws.amazon.com/ses) — 🔵 Freemium

Highly scalable, low-cost transactional email service from AWS, often used as a backend by other ESPs.

- **Free tier:** 62,000 emails/month free when sent from an EC2-hosted application (first 12 months).
- **Paid from:** $0.10 per 1,000 emails beyond free tier.
- **Tags:** `email` `transactional` `aws` `low-cost`
- *Last verified: 2026-05-01*

### [Twilio](https://www.twilio.com) — 🔵 Freemium

SMS, voice, video, and WhatsApp messaging APIs, the most widely integrated communications platform.

- **Free tier:** Free trial credit for new accounts; no perpetual free production tier.
- **Paid from:** Pay-as-you-go per message/minute, varies by country.
- **Tags:** `sms` `voice` `whatsapp` `api`
- *Last verified: 2026-06-01*

### [Vonage (Nexmo)](https://www.vonage.com/communications-apis) — 🔵 Freemium

SMS, voice, and verification APIs, similar in scope to Twilio with competitive per-message pricing.

- **Free tier:** Trial credit for new accounts.
- **Paid from:** Pay-as-you-go per message/minute.
- **Tags:** `sms` `voice` `verification`
- *Last verified: 2026-04-01*

### [OneSignal](https://onesignal.com) — 🔵 Freemium

Push notifications, in-app messaging, and email for mobile and web apps.

- **Free tier:** Free for up to 10,000 subscribers on push notifications.
- **Paid from:** Growth plan billed by subscriber count beyond free tier.
- **Tags:** `push-notifications` `mobile` `in-app-messaging`
- *Last verified: 2026-04-01*

### [Loops](https://loops.so) — 🔵 Freemium

Email platform purpose-built for SaaS startups, combining transactional and marketing email in one tool.

- **Free tier:** Free tier up to 1,000 contacts and 2,500 emails/month.
- **Paid from:** Basic plan from $35/month.
- **Tags:** `email` `saas` `marketing-email`
- *Last verified: 2026-04-01*

### [Plunk](https://www.useplunk.com) — 🔵 Freemium

Open-source-friendly transactional and marketing email platform for startups and indie developers.

- **Free tier:** Free tier with limited monthly email sends.
- **Paid from:** Pro plan billed monthly beyond free quota.
- **Tags:** `email` `open-source` `marketing-email`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Feature Flags & Experimentation

Feature flag management and A/B testing platforms for controlled, gradual feature rollouts.

### [LaunchDarkly](https://launchdarkly.com) — 🔵 Freemium

The most established feature flag management platform, with targeting rules, experimentation, and audit logs.

- **Free tier:** Free tier for up to 1,000 monthly context instances (small projects).
- **Paid from:** Foundation plan billed per seat/usage.
- **Tags:** `feature-flags` `experimentation` `rollouts`
- *Last verified: 2026-04-01*

### [PostHog Feature Flags](https://posthog.com/feature-flags) — 🔵 Freemium

Feature flagging built into the broader PostHog product analytics suite, with usage-based pricing.

- **Free tier:** 1M flag requests/month free (shared with PostHog's overall free event quota).
- **Paid from:** Pay-as-you-go beyond free monthly quota.
- **Tags:** `feature-flags` `open-source` `product-analytics`
- *Last verified: 2026-05-01*

### [Flagsmith](https://www.flagsmith.com) — 🔵 Freemium

Open-source feature flag and remote config platform, self-hostable or managed cloud.

- **Free tier:** Self-hosted fully free; cloud free tier includes 50,000 API requests/month.
- **Paid from:** Startup plan from $45/month.
- **Tags:** `feature-flags` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [Unleash](https://www.getunleash.io) — 🔵 Freemium

Open-source feature flag platform built for enterprise-scale rollouts, with a strong self-hosted option.

- **Free tier:** Self-hosted Open Source edition fully free; Unleash Cloud free tier for small teams.
- **Paid from:** Pro plan billed monthly.
- **Tags:** `feature-flags` `open-source` `enterprise`
- *Last verified: 2026-04-01*

### [Statsig](https://statsig.com) — 🔵 Freemium

Feature flags, experimentation, and product analytics in one platform, built by ex-Facebook engineers.

- **Free tier:** Free tier with generous monthly event allowance.
- **Paid from:** Pay-as-you-go billing beyond free quota.
- **Tags:** `feature-flags` `experimentation` `analytics`
- *Last verified: 2026-04-01*

### [GrowthBook](https://www.growthbook.io) — 🔵 Freemium

Open-source feature flagging and A/B testing platform with a focus on warehouse-native analytics.

- **Free tier:** Self-hosted fully free; cloud free tier for small teams.
- **Paid from:** Pro plan billed monthly.
- **Tags:** `feature-flags` `ab-testing` `open-source`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Forms, Surveys & Customer Feedback

Form builders, survey tools, and feedback widgets for collecting structured input from users.

### [Tally](https://tally.so) — 🔵 Freemium

Notion-like form builder with unlimited free forms and responses, no watermark on the free tier.

- **Free tier:** Unlimited forms and submissions free, no branding required.
- **Paid from:** Pro plan from $29/month for advanced logic/integrations.
- **Tags:** `forms` `surveys` `no-code`
- *Last verified: 2026-05-01*

### [Typeform](https://www.typeform.com) — 🔵 Freemium

Conversational, one-question-at-a-time forms with polished design and branching logic.

- **Free tier:** Free plan: unlimited typeforms, 10 responses/month.
- **Paid from:** Basic plan from $25/month.
- **Tags:** `forms` `surveys` `conversational-ui`
- *Last verified: 2026-04-01*

### [Google Forms](https://www.google.com/forms/about) — 🟢 Free

Free, simple form/survey builder integrated with Google Sheets for response collection.

- **Free tier:** Completely free with a Google account, unlimited forms and responses.
- **Tags:** `forms` `surveys` `google`
- *Last verified: 2026-04-01*

### [Formspree](https://formspree.io) — 🔵 Freemium

Backend-as-a-service for HTML forms — handles submissions, spam filtering, and email notifications without server code.

- **Free tier:** 50 submissions/month free.
- **Paid from:** Starter plan from $10/month.
- **Tags:** `forms` `backend-as-a-service` `static-sites`
- *Last verified: 2026-04-01*

### [Getform](https://getform.io) — 🔵 Freemium

Form endpoint service for static sites and JAMstack apps, with spam filtering and file upload support.

- **Free tier:** 50 submissions/month free, 1 form endpoint.
- **Paid from:** Basic plan from $9/month.
- **Tags:** `forms` `backend-as-a-service` `jamstack`
- *Last verified: 2026-03-01*

### [Canny](https://canny.io) — 🔵 Freemium

Feature request and feedback board for product teams to collect, prioritize, and close the loop with users.

- **Free tier:** Starter plan free for small teams with limited tracked users.
- **Paid from:** Growth plan from $79/month.
- **Tags:** `feedback` `feature-requests` `product-management`
- *Last verified: 2026-04-01*

### [Hotjar](https://www.hotjar.com) — 🔵 Freemium

Heatmaps, session recordings, and on-site surveys for understanding user behavior.

- **Free tier:** Basic plan free with limited daily sessions tracked.
- **Paid from:** Plus plan from $39/month.
- **Tags:** `heatmaps` `session-recording` `ux-research`
- *Last verified: 2026-04-01*

### [SurveyMonkey](https://www.surveymonkey.com) — 🔵 Freemium

Established survey platform with templates, logic branching, and analysis tools.

- **Free tier:** Free plan: up to 10 questions and 25 responses per survey.
- **Paid from:** Standard plan from $25/month.
- **Tags:** `surveys` `market-research`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Headless CMS & Content Management

API-first content management systems for decoupled front-end delivery (web, mobile, JAMstack).

### [Contentful](https://www.contentful.com) — 🔵 Freemium

API-first headless CMS with flexible content modeling and a large app/integration marketplace.

- **Free tier:** Free tier for up to 5 users, 25k records, 2 locales.
- **Paid from:** Basic plan from $300/month.
- **Tags:** `headless-cms` `api-first` `content-modeling`
- *Last verified: 2026-05-01*

### [Sanity](https://www.sanity.io) — 🔵 Freemium

Structured content platform with a real-time collaborative editor and a highly customizable Studio UI.

- **Free tier:** Free tier with 3 users, 10k documents, 5GB assets.
- **Paid from:** Growth plan from $15/month.
- **Tags:** `headless-cms` `real-time` `customizable`
- *Last verified: 2026-05-01*

### [Strapi](https://strapi.io) — 🟣 Open Source

Open-source, self-hostable Node.js headless CMS with a fully customizable admin panel and REST/GraphQL APIs.

- **Free tier:** Community edition completely free, self-hosted.
- **Paid from:** Strapi Cloud from $15/month for managed hosting.
- **Tags:** `headless-cms` `open-source` `self-hosted` `nodejs`
- *Last verified: 2026-05-01*

### [Prismic](https://prismic.io) — 🔵 Freemium

Headless CMS with a visual page builder (Slice Machine) for marketing teams and developers together.

- **Free tier:** Community plan: 1 user, unlimited API calls, documents, and custom types.
- **Paid from:** Starter plan from $7/month/user.
- **Tags:** `headless-cms` `visual-builder` `marketing`
- *Last verified: 2026-04-01*

### [Kontent.ai](https://kontent.ai) — 🔵 Freemium

Content-as-a-Service platform balancing headless CMS benefits with marketer-friendly authoring tools.

- **Free tier:** Developer plan: 2 users, unlimited projects, 2 environments each, 500 content items, 2 languages.
- **Paid from:** Business plan billed annually, custom pricing.
- **Tags:** `headless-cms` `content-as-a-service`
- *Last verified: 2026-03-01*

### [Directus](https://directus.io) — 🟣 Open Source

Open-source data platform that wraps any SQL database with a REST/GraphQL API and admin app instantly.

- **Free tier:** Fully free and open source, self-hosted.
- **Paid from:** Directus Cloud from $15/month for managed hosting.
- **Tags:** `headless-cms` `open-source` `database-wrapper`
- *Last verified: 2026-04-01*

### [Forestry.io](https://forestry.io) — 🔵 Freemium

Git-based headless CMS giving content editors a friendly UI over markdown content in a Git repo.

- **Free tier:** Free for up to 3 sites, 3 editors, with instant previews.
- **Paid from:** Paid plans add more sites/editors.
- **Tags:** `headless-cms` `git-based` `markdown`
- *Last verified: 2026-02-01*

### [Builder.io](https://www.builder.io) — 🔵 Freemium

Visual headless CMS and drag-and-drop page builder that integrates with React, Vue, and other frameworks.

- **Free tier:** Free tier for individuals with limited monthly sessions/seats.
- **Paid from:** Growth plan billed monthly.
- **Tags:** `headless-cms` `visual-builder` `page-builder`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Learning, Education & Student Developer Packs

Free learning platforms, certification prep, and bundled developer tool packs for students and educators.

### [GitHub Student Developer Pack](https://education.github.com/pack) — 🟢 Free

Bundle of free access/credits to dozens of developer tools (domains, hosting, APIs, IDEs) for verified students.

- **Free tier:** Free for the duration of verified student status; bundle composition changes periodically.
- **Tags:** `student-pack` `bundled-offers` `education`
- *Last verified: 2026-05-01*

### [freeCodeCamp](https://www.freecodecamp.org) — 🟢 Free

Full-length, project-based curriculum covering web development, data science, and more, with free certifications.

- **Free tier:** 100% free, nonprofit, ad-light platform.
- **Tags:** `learning` `free-certifications` `nonprofit`
- *Last verified: 2026-05-01*

### [The Odin Project](https://www.theodinproject.com) — 🟢 Free

Free, open-source full-stack web development curriculum built and maintained by its community.

- **Free tier:** Completely free, open source curriculum.
- **Tags:** `learning` `open-source` `full-stack`
- *Last verified: 2026-04-01*

### [MDN Web Docs](https://developer.mozilla.org) — 🟢 Free

Mozilla's comprehensive, authoritative reference documentation for HTML, CSS, JavaScript, and web APIs.

- **Free tier:** Completely free reference and learning content.
- **Tags:** `documentation` `reference` `web-standards`
- *Last verified: 2026-05-01*

### [Roadmap.sh](https://roadmap.sh) — 🔵 Freemium

Community-driven learning roadmaps for dozens of tech career paths, with interactive guides and projects.

- **Free tier:** Free roadmaps and guides; some premium courses/projects are paid.
- **Paid from:** Pro plan from ~$9/month for premium content.
- **Tags:** `learning` `roadmaps` `career-paths`
- *Last verified: 2026-04-01*

### [Exercism](https://exercism.org) — 🟢 Free

Free coding exercises across 70+ languages with human mentoring feedback on submitted solutions.

- **Free tier:** Completely free, nonprofit-backed.
- **Tags:** `learning` `coding-exercises` `mentoring`
- *Last verified: 2026-04-01*

### [Coursera (Financial Aid / Free Audits)](https://www.coursera.org) — 🔵 Freemium

University-partnered courses and certificates; most courses can be audited free, with paid certificates.

- **Free tier:** Free audit access to course materials (no certificate) for most courses.
- **Paid from:** Specializations from ~$49/month, or pay-per-course certificates.
- **Tags:** `learning` `university-courses` `certificates`
- *Last verified: 2026-03-01*

### [Khan Academy](https://www.khanacademy.org) — 🟢 Free

Free courses spanning computer science fundamentals, math, and more, run by a nonprofit.

- **Free tier:** 100% free, nonprofit.
- **Tags:** `learning` `nonprofit` `computer-science`
- *Last verified: 2026-03-01*

### [LeetCode](https://leetcode.com) — 🔵 Freemium

Coding interview practice platform with thousands of algorithm/data-structure problems.

- **Free tier:** Free tier with access to most problems and basic discussion forums.
- **Paid from:** Premium plan from $35/month for company-tagged problems and extra solutions.
- **Tags:** `interview-prep` `algorithms` `practice-problems`
- *Last verified: 2026-04-01*

### [JetBrains Student License](https://www.jetbrains.com/community/education) — 🟢 Free

Free access to the full JetBrains IDE suite (IntelliJ, PyCharm, WebStorm, etc.) for verified students/educators.

- **Free tier:** Free for the duration of verified academic status.
- **Tags:** `ide` `student-license` `jetbrains`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Low-Code, No-Code & Automation

Workflow automation, integration platforms, and no-code/low-code app builders.

### [Zapier](https://zapier.com) — 🔵 Freemium

The original no-code automation platform connecting thousands of apps with trigger-action workflows.

- **Free tier:** 100 tasks/month free, single-step Zaps only.
- **Paid from:** Starter plan from $19.99/month.
- **Tags:** `automation` `no-code` `integrations`
- *Last verified: 2026-05-01*

### [Make (formerly Integromat)](https://www.make.com) — 🔵 Freemium

Visual workflow automation builder with more granular branching/looping logic than typical no-code tools.

- **Free tier:** 1,000 operations/month free.
- **Paid from:** Core plan from $9/month.
- **Tags:** `automation` `no-code` `visual-workflows`
- *Last verified: 2026-05-01*

### [n8n](https://n8n.io) — 🔵 Freemium

Open-source, self-hostable workflow automation tool with a fair-code license and code-step support.

- **Free tier:** Self-hosted is free and unlimited; n8n Cloud has a free trial.
- **Paid from:** Cloud Starter plan from $20/month.
- **Tags:** `automation` `open-source` `self-hosted` `fair-code`
- *Last verified: 2026-05-01*

### [Pipedream](https://pipedream.com) — 🔵 Freemium

Developer-focused integration platform combining low-code workflows with full code-step flexibility.

- **Free tier:** 10,000 invocations/month free.
- **Paid from:** Basic plan from $19/month.
- **Tags:** `automation` `developer-focused` `code-steps`
- *Last verified: 2026-04-01*

### [Bubble](https://bubble.io) — 🔵 Freemium

No-code platform for building full web applications visually, including database and workflow logic.

- **Free tier:** Free plan for personal/learning projects (Bubble branding, limited capacity).
- **Paid from:** Starter plan from $32/month.
- **Tags:** `no-code` `app-builder` `database`
- *Last verified: 2026-04-01*

### [Retool](https://retool.com) — 🔵 Freemium

Low-code platform for building internal tools and admin dashboards quickly by connecting to existing data sources.

- **Free tier:** Free for up to 5 users.
- **Paid from:** Team plan from $10/user/month.
- **Tags:** `low-code` `internal-tools` `admin-dashboards`
- *Last verified: 2026-05-01*

### [Airtable](https://www.airtable.com) — 🔵 Freemium

Spreadsheet-database hybrid with automation, forms, and views, used for lightweight app-like workflows.

- **Free tier:** Free plan: 1,000 records/base, 1GB attachments/base.
- **Paid from:** Team plan from $20/seat/month.
- **Tags:** `no-code` `database` `spreadsheet`
- *Last verified: 2026-05-01*

### [Activepieces](https://www.activepieces.com) — 🟣 Open Source

Open-source Zapier alternative for business automation, extensible with custom TypeScript pieces.

- **Free tier:** Self-hosted fully free; cloud has a free tier with limited tasks.
- **Paid from:** Cloud plans billed monthly.
- **Tags:** `automation` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [Coupler.io](https://www.coupler.io) — 🔵 Freemium

Data integration tool that syncs data between apps, spreadsheets, and BI dashboards on a schedule.

- **Free tier:** Free tier with limited scheduled syncs.
- **Paid from:** Personal plan from $49/month.
- **Tags:** `data-integration` `etl` `automation`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Monitoring, Logging & Observability

Application performance monitoring, error tracking, log aggregation, and uptime monitoring services.

### [Sentry](https://sentry.io) — 🔵 Freemium

Error tracking and performance monitoring across web, mobile, and backend stacks with rich stack-trace context.

- **Free tier:** 5,000 errors/month, 1 team member, 1 project on free Developer plan.
- **Paid from:** Team plan from $26/month.
- **Tags:** `error-tracking` `apm` `observability`
- *Last verified: 2026-06-01*

### [Better Stack (formerly Better Uptime / Logtail)](https://betterstack.com) — 🔵 Freemium

Combined uptime monitoring, incident management, and log management platform with on-call alerting.

- **Free tier:** Free tier covers limited monitors, log volume, and status pages.
- **Paid from:** Paid plans scale with monitors/log volume.
- **Tags:** `uptime-monitoring` `logging` `incident-management`
- *Last verified: 2026-05-01*

### [UptimeRobot](https://uptimerobot.com) — 🔵 Freemium

Simple uptime monitoring with email/SMS alerts and public status pages.

- **Free tier:** 50 monitors, 5-minute check intervals free.
- **Paid from:** Pro plans from $7/month for 1-minute intervals.
- **Tags:** `uptime-monitoring` `alerting` `status-page`
- *Last verified: 2026-05-01*

### [Grafana Cloud](https://grafana.com/products/cloud) — 🔵 Freemium

Managed Grafana, Prometheus (metrics), Loki (logs), and Tempo (traces) for full-stack observability.

- **Free tier:** Free tier includes 10k metrics series, 50GB logs, 50GB traces per month.
- **Paid from:** Pro plan billed on usage beyond free quota.
- **Tags:** `metrics` `logs` `traces` `prometheus` `grafana`
- *Last verified: 2026-06-01*

### [New Relic](https://newrelic.com) — 🔵 Freemium

Full-stack observability platform covering APM, infrastructure, logs, and browser/mobile monitoring.

- **Free tier:** 100GB data ingest/month free, one full-access user.
- **Paid from:** Pay-as-you-go beyond included data ingest.
- **Tags:** `apm` `infrastructure-monitoring` `logs`
- *Last verified: 2026-05-01*

### [Datadog](https://www.datadoghq.com) — 🔵 Freemium

Comprehensive monitoring platform for infrastructure, APM, logs, security, and synthetic testing.

- **Free tier:** Free tier for up to 5 hosts with 1-day metric retention.
- **Paid from:** Pro plan from $15/host/month.
- **Tags:** `apm` `infrastructure-monitoring` `logs` `security`
- *Last verified: 2026-06-01*

### [LogRocket](https://logrocket.com) — 🔵 Freemium

Session replay combined with frontend error/performance monitoring to see exactly what users experienced.

- **Free tier:** 1,000 sessions/month free.
- **Paid from:** Team plan from $99/month.
- **Tags:** `session-replay` `frontend-monitoring` `error-tracking`
- *Last verified: 2026-04-01*

### [Highlight.io](https://www.highlight.io) — 🔵 Freemium

Open-source session replay, error monitoring, and logging platform, self-hostable or cloud-managed.

- **Free tier:** Free tier with limited monthly sessions and log/error events.
- **Paid from:** Paid plans scale with session/event volume.
- **Tags:** `session-replay` `open-source` `logging`
- *Last verified: 2026-04-01*

### [Checkly](https://www.checklyhq.com) — 🔵 Freemium

Synthetic monitoring and API/E2E testing built on Playwright, with monitoring-as-code workflows.

- **Free tier:** Free tier includes limited check runs/month.
- **Paid from:** Team plan billed on check volume.
- **Tags:** `synthetic-monitoring` `playwright` `api-testing`
- *Last verified: 2026-04-01*

### [PagerDuty](https://www.pagerduty.com) — 🔵 Freemium

Incident response and on-call alerting platform integrating with most monitoring tools.

- **Free tier:** Free tier for up to 5 users with basic on-call scheduling.
- **Paid from:** Professional plan from $21/user/month.
- **Tags:** `incident-management` `on-call` `alerting`
- *Last verified: 2026-04-01*

### [OpenTelemetry](https://opentelemetry.io) — 🟣 Open Source

Vendor-neutral open-source standard and SDKs for collecting traces, metrics, and logs across services.

- **Free tier:** Fully free and open source; pairs with any backend (Jaeger, Prometheus, Grafana, vendor platforms).
- **Tags:** `tracing` `metrics` `open-source` `standard`
- *Last verified: 2026-05-01*

### [Jaeger](https://www.jaegertracing.io) — 🟣 Open Source

Open-source, self-hosted distributed tracing system originally built by Uber, CNCF graduated project.

- **Free tier:** Completely free, self-hosted.
- **Tags:** `tracing` `distributed-systems` `self-hosted` `cncf`
- *Last verified: 2026-05-01*

[⬆️ Back to Top](#table-of-contents)

## Object & File Storage

Cloud object storage, file sync/sharing, and backup services for application and personal data.

### [Amazon S3](https://aws.amazon.com/s3) — 🔵 Freemium

Industry-standard object storage with virtually unlimited scalability and deep AWS ecosystem integration.

- **Free tier:** 5GB standard storage, 20,000 GET / 2,000 PUT requests free for 12 months.
- **Paid from:** Pay-as-you-go from ~$0.023/GB/month after free tier.
- **Tags:** `object-storage` `aws` `s3-compatible`
- *Last verified: 2026-06-01*

### [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2) — 🔵 Freemium

S3-compatible object storage with zero egress fees, ideal for serving large files without bandwidth surprises.

- **Free tier:** 10GB storage free/month, 1M Class A and 10M Class B operations free/month.
- **Paid from:** $0.015/GB storage beyond free tier; no egress charges ever.
- **Tags:** `object-storage` `s3-compatible` `no-egress-fees`
- *Last verified: 2026-06-01*

### [Backblaze B2](https://www.backblaze.com/cloud-storage) — 🔵 Freemium

Low-cost S3-compatible object storage, popular for backups and media storage with free egress to many CDNs.

- **Free tier:** 10GB storage free.
- **Paid from:** $6/TB/month beyond free tier.
- **Tags:** `object-storage` `backup` `low-cost`
- *Last verified: 2026-05-01*

### [Wasabi](https://wasabi.com) — 🔵 Freemium

Flat-rate S3-compatible cloud storage with no egress or API request fees.

- **Free tier:** 30-day free trial with 1TB; no perpetual free tier.
- **Paid from:** Flat $5.99/TB/month (no egress fees).
- **Tags:** `object-storage` `s3-compatible` `flat-rate`
- *Last verified: 2026-04-01*

### [Google Cloud Storage](https://cloud.google.com/storage) — 🔵 Freemium

Google's object storage with multiple storage classes (Standard, Nearline, Coldline, Archive) for tiered cost.

- **Free tier:** 5GB-months Standard storage free, 5,000 Class A and 50,000 Class B ops free/month.
- **Paid from:** Pay-as-you-go from $0.020/GB/month after free tier.
- **Tags:** `object-storage` `google` `tiered-storage`
- *Last verified: 2026-05-01*

### [Uploadcare](https://uploadcare.com) — 🔵 Freemium

File uploading, storage, and on-the-fly image/video processing API with a CDN-backed delivery layer.

- **Free tier:** Free tier includes limited monthly uploads and storage.
- **Paid from:** Paid plans from $59/month.
- **Tags:** `file-upload` `image-processing` `cdn`
- *Last verified: 2026-04-01*

### [Cloudinary](https://cloudinary.com) — 🔵 Freemium

Media management platform for image/video upload, storage, transformation, and optimized delivery.

- **Free tier:** 25 monthly credits free, covering a generous mix of storage, transformations, and bandwidth.
- **Paid from:** Plus plan from $99/month.
- **Tags:** `image-processing` `video-processing` `cdn` `media-management`
- *Last verified: 2026-05-01*

### [ImageKit](https://imagekit.io) — 🔵 Freemium

Real-time image and video optimization/CDN service with URL-based transformations.

- **Free tier:** 20GB bandwidth and storage combined free/month.
- **Paid from:** Growth plan from $49/month.
- **Tags:** `image-processing` `video-processing` `cdn`
- *Last verified: 2026-04-01*

### [Dropbox](https://www.dropbox.com) — 🔵 Freemium

File sync and sharing service, also offers a developer API for app-integrated storage.

- **Free tier:** 2GB free storage.
- **Paid from:** Plus plan from $11.99/month for 2TB.
- **Tags:** `file-sync` `personal-storage` `api`
- *Last verified: 2026-03-01*

### [Filebase](https://filebase.com) — 🔵 Freemium

S3-compatible storage backed by decentralized networks (IPFS, Sia, Storj) accessed through a standard API.

- **Free tier:** 5GB free storage on decentralized backends.
- **Paid from:** Paid plans from $5.99/month.
- **Tags:** `object-storage` `decentralized` `ipfs` `s3-compatible`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Payments & Billing

Payment processing, subscription billing, and invoicing APIs for monetizing applications.

### [Stripe](https://stripe.com) — 🔵 Freemium

The most widely integrated payments platform: checkout, subscriptions, invoicing, and a powerful API.

- **Free tier:** No monthly fee; pay only per successful transaction (no free transaction quota).
- **Paid from:** 2.9% + $0.30 per successful card transaction (US rates).
- **Tags:** `payments` `subscriptions` `checkout` `api`
- *Last verified: 2026-06-01*

### [Paddle](https://www.paddle.com) — 🔵 Freemium

Merchant-of-record billing platform handling global tax/VAT compliance for SaaS subscriptions.

- **Free tier:** No monthly fee; pay per transaction only.
- **Paid from:** 5% + $0.50 per transaction (varies by plan).
- **Tags:** `payments` `merchant-of-record` `tax-compliance` `saas`
- *Last verified: 2026-05-01*

### [Lemon Squeezy](https://www.lemonsqueezy.com) — 🔵 Freemium

Merchant-of-record platform for selling software/digital products with built-in tax handling, popular with indie devs.

- **Free tier:** No monthly fee; pay per transaction only.
- **Paid from:** 5% + $0.50 per transaction.
- **Tags:** `payments` `merchant-of-record` `indie-devs` `digital-products`
- *Last verified: 2026-05-01*

### [PayPal Developer](https://developer.paypal.com) — 🔵 Freemium

Widely recognized payment buttons and checkout API with strong consumer trust/brand recognition.

- **Free tier:** No monthly fee; pay only per transaction.
- **Paid from:** Standard rate ~3.49% + fixed fee per transaction (varies by region).
- **Tags:** `payments` `checkout` `consumer-trust`
- *Last verified: 2026-04-01*

### [Razorpay](https://razorpay.com) — 🔵 Freemium

Payments and business banking platform focused on the Indian market, supports UPI, cards, and netbanking.

- **Free tier:** No setup/monthly fee; pay only per transaction.
- **Paid from:** Standard rate ~2% per domestic transaction.
- **Tags:** `payments` `india` `upi`
- *Last verified: 2026-04-01*

### [Wise Platform](https://wise.com/platform) — 🔵 Freemium

Cross-border payments API for sending international transfers at near-real exchange rates.

- **Free tier:** No subscription fee; pay variable rates per international transfer.
- **Tags:** `payments` `cross-border` `fx`
- *Last verified: 2026-03-01*

### [Chargebee](https://www.chargebee.com) — 🔵 Freemium

Subscription billing and revenue management platform handling complex pricing models and dunning.

- **Free tier:** Free tier for businesses with under $250k in annual recurring billing.
- **Paid from:** Performance plan billed on revenue beyond free threshold.
- **Tags:** `billing` `subscriptions` `revenue-management`
- *Last verified: 2026-04-01*

### [Commerce Layer](https://commercelayer.io) — 🔵 Freemium

Composable commerce API for building, placing, and managing orders from any frontend.

- **Free tier:** Developer plan free: 100 orders/month, up to 1,000 SKUs.
- **Paid from:** Paid plans scale with order volume.
- **Tags:** `ecommerce` `composable-commerce` `api`
- *Last verified: 2026-04-01*

[⬆️ Back to Top](#table-of-contents)

## Project Management & Team Collaboration

Issue tracking, kanban boards, wikis, and team chat/collaboration tools.

### [Jira](https://www.atlassian.com/software/jira) — 🔵 Freemium

Atlassian's issue tracking and agile project management tool, the de facto standard at many software companies.

- **Free tier:** Free for up to 10 users with core features.
- **Paid from:** Standard plan from $7.75/user/month.
- **Tags:** `issue-tracking` `agile` `kanban` `scrum`
- *Last verified: 2026-05-01*

### [Trello](https://trello.com) — 🔵 Freemium

Simple kanban-style board tool for personal and small-team task management.

- **Free tier:** Unlimited cards, up to 10 boards per workspace free.
- **Paid from:** Standard plan from $5/user/month.
- **Tags:** `kanban` `task-management`
- *Last verified: 2026-05-01*

### [Linear](https://linear.app) — 🔵 Freemium

Fast, keyboard-driven issue tracking and project management built for software teams.

- **Free tier:** Free for up to 250 issues with core features for small teams.
- **Paid from:** Basic plan from $8/user/month.
- **Tags:** `issue-tracking` `software-teams` `fast-ui`
- *Last verified: 2026-06-01*

### [Notion](https://www.notion.com) — 🔵 Freemium

All-in-one workspace combining docs, wikis, databases, and project tracking.

- **Free tier:** Free for individuals with unlimited blocks; limited file uploads and collaborators on team free plan.
- **Paid from:** Plus plan from $10/user/month.
- **Tags:** `docs` `wiki` `database` `all-in-one`
- *Last verified: 2026-06-01*

### [ClickUp](https://clickup.com) — 🔵 Freemium

Highly customizable project management platform combining tasks, docs, goals, and whiteboards.

- **Free tier:** Free Forever plan with unlimited users and tasks, limited storage.
- **Paid from:** Unlimited plan from $7/user/month.
- **Tags:** `project-management` `docs` `customizable`
- *Last verified: 2026-05-01*

### [Huly](https://huly.io) — 🔵 Freemium

All-in-one open-source project management platform (Linear/Jira/Slack/Notion alternative) with chat and video built in.

- **Free tier:** Unlimited users, 10GB storage/workspace, 10GB video/audio traffic free.
- **Paid from:** Paid plans add higher storage and SSO.
- **Tags:** `project-management` `open-source` `chat` `all-in-one`
- *Last verified: 2026-05-01*

### [Slack](https://slack.com) — 🔵 Freemium

Team chat and collaboration hub with channels, threads, and a vast app/integration ecosystem.

- **Free tier:** 90-day searchable message history, unlimited integrations, free for small teams.
- **Paid from:** Pro plan from $7.25/user/month.
- **Tags:** `team-chat` `collaboration` `integrations`
- *Last verified: 2026-05-01*

### [Discord](https://discord.com) — 🟢 Free

Voice, video, and text chat platform, widely adopted by dev communities and open-source projects.

- **Free tier:** Free for unlimited servers, messages, and voice/video, with no message history limit.
- **Paid from:** Nitro subscription adds cosmetic/upload perks, not required for core use.
- **Tags:** `team-chat` `voice-chat` `community`
- *Last verified: 2026-05-01*

### [Gitter](https://gitter.im) — 🔵 Freemium

Chat tool built for GitHub projects and open-source communities.

- **Free tier:** Unlimited public/private rooms, free for teams up to 25.
- **Tags:** `team-chat` `github` `open-source`
- *Last verified: 2026-02-01*

### [HackMD](https://hackmd.io) — 🔵 Freemium

Real-time collaborative markdown editing, like Google Docs but for markdown notes and docs.

- **Free tier:** Unlimited notes free; collaborator count limited on private notes/templates.
- **Paid from:** Pro plan from $5/month for more collaborators.
- **Tags:** `markdown` `collaborative-editing` `docs`
- *Last verified: 2026-03-01*

### [GoKanban.io](https://gokanban.io) — 🟢 Free

Syntax-based, no-registration kanban board for quick personal task tracking.

- **Free tier:** Completely free, no account required, no limitations.
- **Tags:** `kanban` `no-signup` `lightweight`
- *Last verified: 2026-02-01*

### [HeySpace](https://hey.space) — 🔵 Freemium

Task management with integrated chat, calendar, timeline view, and video calls.

- **Free tier:** Free for up to 5 users.
- **Paid from:** Basic plan from $6.7/user/month.
- **Tags:** `task-management` `chat` `calendar`
- *Last verified: 2026-02-01*

[⬆️ Back to Top](#table-of-contents)

## Search & Analytics

Hosted search engines and product/web analytics platforms.

### [Algolia](https://www.algolia.com) — 🔵 Freemium

Fast, hosted search-as-a-service API with typo tolerance, faceting, and instant-search UI components.

- **Free tier:** Free tier (Build): 10,000 search requests/month, 100k records.
- **Paid from:** Grow plan billed on usage above free tier.
- **Tags:** `search` `saas` `instant-search`
- *Last verified: 2026-05-01*

### [Meilisearch](https://www.meilisearch.com) — 🔵 Freemium

Open-source, fast search engine with a managed cloud option; self-hosted is fully free.

- **Free tier:** Free self-hosted; Cloud free trial credits for new accounts.
- **Paid from:** Cloud plans billed on usage.
- **Tags:** `search` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [Typesense](https://typesense.org) — 🔵 Freemium

Open-source, typo-tolerant search engine optimized for speed, with a managed Typesense Cloud option.

- **Free tier:** Free self-hosted; Cloud has a free tier for small clusters.
- **Paid from:** Cloud plans billed hourly per cluster size.
- **Tags:** `search` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [Elastic Cloud](https://www.elastic.co/cloud) — 🔵 Freemium

Managed Elasticsearch, Kibana, and the full Elastic Stack for search, logging, and observability.

- **Free tier:** 14-day free trial; self-managed Elasticsearch core remains free/open under Elastic license.
- **Paid from:** Standard plan billed hourly on cloud usage.
- **Tags:** `search` `elasticsearch` `logging` `observability`
- *Last verified: 2026-04-01*

### [Plausible Analytics](https://plausible.io) — 🔵 Freemium

Lightweight, privacy-focused, cookie-free web analytics, open source with a hosted option.

- **Free tier:** 30-day free trial; self-hosted community edition is free.
- **Paid from:** Hosted plans from $9/month for up to 10k pageviews.
- **Tags:** `web-analytics` `privacy-focused` `open-source`
- *Last verified: 2026-05-01*

### [Umami](https://umami.is) — 🔵 Freemium

Simple, open-source, privacy-friendly web analytics as a self-hosted alternative to Google Analytics.

- **Free tier:** Free self-hosted; Umami Cloud has a free tier for up to 100k events/month.
- **Paid from:** Cloud Pro plan from $20/month.
- **Tags:** `web-analytics` `open-source` `privacy-focused`
- *Last verified: 2026-04-01*

### [PostHog](https://posthog.com) — 🔵 Freemium

Open-source product analytics suite: event tracking, session replay, feature flags, and A/B testing in one platform.

- **Free tier:** 1M events/month free, 5k session replays/month free.
- **Paid from:** Pay-as-you-go billing beyond free monthly quotas.
- **Tags:** `product-analytics` `open-source` `session-replay` `feature-flags`
- *Last verified: 2026-06-01*

### [Mixpanel](https://mixpanel.com) — 🔵 Freemium

Product analytics platform focused on event-based funnels, retention, and cohort analysis.

- **Free tier:** 20M events/month free on the free tier.
- **Paid from:** Growth plan billed on monthly tracked users.
- **Tags:** `product-analytics` `funnels` `retention`
- *Last verified: 2026-04-01*

### [Google Analytics](https://marketingplatform.google.com/about/analytics) — 🟢 Free

Google's widely used web/app analytics platform (GA4), tracking traffic, behavior, and conversions.

- **Free tier:** Free with generous usage limits for the vast majority of sites.
- **Tags:** `web-analytics` `google` `ga4`
- *Last verified: 2026-05-01*

[⬆️ Back to Top](#table-of-contents)

## Secrets Management & Security

Secrets/config management, vulnerability scanning, and application security testing services.

### [Doppler](https://www.doppler.com) — 🔵 Freemium

Universal secrets manager for application secrets and config, syncing to most cloud providers and CI tools.

- **Free tier:** Free for unlimited users with basic access controls and config syncing.
- **Paid from:** Team plan billed per seat for advanced access controls.
- **Tags:** `secrets-management` `config-management`
- *Last verified: 2026-04-01*

### [HashiCorp Vault (HCP Vault)](https://www.hashicorp.com/products/vault) — 🔵 Freemium

Industry-standard secrets management and encryption-as-a-service, available self-hosted (free OSS) or as managed HCP Vault.

- **Free tier:** Self-hosted OSS edition fully free; HCP Vault has a limited free development tier.
- **Paid from:** HCP Vault plans billed hourly on cluster size.
- **Tags:** `secrets-management` `open-source` `encryption`
- *Last verified: 2026-04-01*

### [Infisical](https://infisical.com) — 🟣 Open Source

Open-source secrets management platform with a managed cloud option, designed as a Doppler/Vault alternative.

- **Free tier:** Self-hosted free; cloud free tier for small teams.
- **Paid from:** Pro plan billed per seat.
- **Tags:** `secrets-management` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [1Password Developer Tools (Secrets Automation)](https://developer.1password.com) — 🔵 Freemium

Secrets automation tooling (CLI, SDKs, Connect server) built on top of 1Password vaults for CI/CD pipelines.

- **Free tier:** Free trial for teams; secrets automation included with paid Business plans.
- **Paid from:** Business plan from $7.99/user/month.
- **Tags:** `secrets-management` `cli` `ci-cd-integration`
- *Last verified: 2026-03-01*

### [Snyk (security scanning)](https://snyk.io) — 🔵 Freemium

Scans code, open-source dependencies, containers, and infrastructure-as-code for vulnerabilities.

- **Free tier:** Free tier with limited monthly tests across products.
- **Paid from:** Team plan from $25/product/month.
- **Tags:** `vulnerability-scanning` `sast` `container-security` `iac-security`
- *Last verified: 2026-06-01*

### [Trivy](https://trivy.dev) — 🟣 Open Source

Open-source, all-in-one vulnerability and misconfiguration scanner for containers, IaC, and filesystems.

- **Free tier:** Completely free and open source.
- **Tags:** `vulnerability-scanning` `open-source` `container-security`
- *Last verified: 2026-04-01*

### [GitGuardian](https://www.gitguardian.com) — 🔵 Freemium

Detects hardcoded secrets and credentials leaked in source code, commit history, and CI logs.

- **Free tier:** Free tier for individual developers and small teams.
- **Paid from:** Business plan billed per developer seat.
- **Tags:** `secrets-detection` `security` `ci-cd-scanning`
- *Last verified: 2026-04-01*

### [Have I Been Pwned API](https://haveibeenpwned.com/API/Key) — 🔴 Paid

API for checking whether an email/password has appeared in known data breaches.

- **Free tier:** N/A — the API requires a paid subscription key as of recent pricing changes.
- **Paid from:** From ~$3.95/month for individual API key.
- **Note:** The public website lookup remains free for individuals; the API itself requires a paid key.
- **Tags:** `breach-detection` `security-api`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Serverless Functions & Backend-as-a-Service

Function-as-a-service compute and backend-as-a-service platforms for event-driven application logic.

### [AWS Lambda](https://aws.amazon.com/lambda) — 🔵 Freemium

Pioneer of serverless functions; runs code in response to events without managing servers.

- **Free tier:** 1M requests/month and 400,000 GB-seconds compute free, always-free (not time-limited).
- **Paid from:** $0.20 per 1M requests beyond free tier.
- **Tags:** `serverless` `faas` `aws` `event-driven`
- *Last verified: 2026-06-01*

### [Google Cloud Functions](https://cloud.google.com/functions) — 🔵 Freemium

Event-driven serverless functions integrated with the Google Cloud and Firebase ecosystems.

- **Free tier:** 2M invocations/month free, always-free.
- **Paid from:** $0.40 per 1M invocations beyond free tier.
- **Tags:** `serverless` `faas` `google-cloud` `firebase`
- *Last verified: 2026-05-01*

### [Azure Functions](https://azure.microsoft.com/products/functions) — 🔵 Freemium

Microsoft's serverless compute service, integrates tightly with the .NET ecosystem and Azure services.

- **Free tier:** 1M requests/month free, always-free.
- **Paid from:** Consumption plan billed per execution beyond free tier.
- **Tags:** `serverless` `faas` `azure` `dotnet`
- *Last verified: 2026-05-01*

### [Cloudflare Workers](https://workers.cloudflare.com) — 🔵 Freemium

V8-isolate-based edge functions with extremely low cold-start latency, running in 300+ global locations.

- **Free tier:** 100,000 requests/day free.
- **Paid from:** Paid plan from $5/month for 10M requests.
- **Tags:** `serverless` `edge-compute` `low-latency`
- *Last verified: 2026-06-01*

### [Vercel Functions](https://vercel.com/docs/functions) — 🔵 Freemium

Serverless and edge functions deeply integrated with Next.js and the Vercel deployment pipeline.

- **Free tier:** Included in the free Hobby plan with limits on execution time/invocations.
- **Paid from:** Pro plan from $20/month for higher limits.
- **Tags:** `serverless` `nextjs` `edge-functions`
- *Last verified: 2026-05-01*

### [Deno Deploy](https://deno.com/deploy) — 🔵 Freemium

Globally distributed serverless JavaScript/TypeScript runtime built on Deno, with zero-config deploys.

- **Free tier:** Free tier with generous request and CPU-time allowances for hobby projects.
- **Paid from:** Pro plan billed per usage beyond free tier.
- **Tags:** `serverless` `deno` `typescript` `edge`
- *Last verified: 2026-04-01*

### [Appwrite](https://appwrite.io) — 🔵 Freemium

Open-source backend-as-a-service with auth, databases, storage, and functions, self-hostable or managed cloud.

- **Free tier:** Self-hosted fully free; Cloud free tier includes generous bandwidth/storage/function execution.
- **Paid from:** Pro plan from $15/month.
- **Tags:** `backend-as-a-service` `open-source` `self-hosted`
- *Last verified: 2026-05-01*

### [Convex](https://www.convex.dev) — 🔵 Freemium

Reactive backend platform combining database, server functions, and real-time sync into one TypeScript-first system.

- **Free tier:** Free tier with generous function calls and database bandwidth for small projects.
- **Paid from:** Professional plan from $25/month.
- **Tags:** `backend-as-a-service` `real-time` `typescript`
- *Last verified: 2026-05-01*

[⬆️ Back to Top](#table-of-contents)

## Source Code Hosting

Git and version control hosting platforms, including code review, issue tracking, and CI integration.

### [GitHub](https://github.com) — 🔵 Freemium

The largest Git hosting platform with issues, project boards, Actions CI/CD, and package registry built in.

- **Free tier:** Unlimited public and private repositories, unlimited collaborators on free plan, 2,000 CI/CD Actions minutes/month, 500MB Packages storage.
- **Paid from:** Team plan from $4/user/month; Enterprise from $21/user/month.
- **Often compared to:** GitLab Self-Managed, Bitbucket
- **Note:** Private repo collaborator limits were removed in 2019; free tier is generous for small teams.
- **Tags:** `git` `vcs` `ci-cd` `code-review` `issues`
- *Last verified: 2026-06-01*

### [GitLab](https://gitlab.com) — 🔵 Freemium

Git hosting with an integrated DevOps platform: CI/CD, container registry, security scanning, and Kubernetes integration.

- **Free tier:** Unlimited private repos, 5 users per top-level namespace free, 400 CI/CD minutes/month, 5GB storage, 10GB transfer.
- **Paid from:** Premium from $29/user/month.
- **Often compared to:** GitHub Enterprise
- **Note:** Also distributed as free open-source self-managed Community Edition.
- **Tags:** `git` `vcs` `ci-cd` `devops` `self-hosted`
- *Last verified: 2026-06-01*

### [Bitbucket](https://bitbucket.org) — 🔵 Freemium

Atlassian's Git hosting product, tightly integrated with Jira and Trello, with built-in Pipelines CI/CD.

- **Free tier:** Unlimited private repos for up to 5 users, 50 build minutes/month on Pipelines.
- **Paid from:** Standard from $3/user/month.
- **Tags:** `git` `vcs` `ci-cd` `jira-integration`
- *Last verified: 2026-06-01*

### [SourceHut](https://sourcehut.org) — 🟣 Open Source

Minimalist, hackable software forge: Git/Mercurial hosting, mailing lists, CI, and issue tracking, all email-driven and ad-free.

- **Free tier:** Pay-what-you-want; free tier available, fully open source and self-hostable.
- **Tags:** `git` `mercurial` `self-hosted` `minimalist` `ci-cd`
- *Last verified: 2026-05-15*

### [Codeberg](https://codeberg.org) — 🟢 Free

Non-profit, community-run Git hosting built on Forgejo (a Gitea fork), as a privacy-respecting GitHub alternative.

- **Free tier:** Unlimited public and private repos, free for individuals and small projects, donation-funded.
- **Tags:** `git` `non-profit` `self-hosted` `privacy`
- *Last verified: 2026-05-15*

### [Gitea (Cloud / Self-host)](https://gitea.com) — 🟣 Open Source

Lightweight, self-hostable Git service; Gitea Cloud offers managed hosting on top of the open-source core.

- **Free tier:** Self-hosted is fully free and open source; Gitea Cloud has a free tier for small repos.
- **Tags:** `git` `self-hosted` `lightweight`
- *Last verified: 2026-05-15*

### [Launchpad](https://launchpad.net) — 🟢 Free

Canonical's collaboration platform for Bazaar/Git hosting, bug tracking, and Ubuntu/PPA package building.

- **Free tier:** Free for open-source projects, including PPA package builds.
- **Tags:** `git` `bazaar` `open-source` `ppa`
- *Last verified: 2026-04-20*

### [SourceForge](https://sourceforge.net) — 🟢 Free

Long-running open-source project hosting with file release distribution, forums, and Git/SVN/Mercurial support.

- **Free tier:** Free hosting and unlimited bandwidth for open-source projects.
- **Tags:** `git` `svn` `open-source` `file-hosting`
- *Last verified: 2026-04-20*

### [jitpack.io](https://jitpack.io) — 🟢 Free

Turns any GitHub repository into a Maven dependency without needing to publish to a separate repository.

- **Free tier:** Free for public projects, unlimited builds.
- **Tags:** `maven` `jvm` `package-registry` `android`
- *Last verified: 2026-04-20*

### [Gemfury](https://gemfury.com) — 🔵 Freemium

Private and public artifact/package repository supporting Maven, PyPI, npm, Go modules, NuGet, APT, and RPM.

- **Free tier:** Free for public packages.
- **Paid from:** Starter plans from ~$7/month for private packages.
- **Tags:** `package-registry` `artifact-repo` `npm` `pypi`
- *Last verified: 2026-04-20*

[⬆️ Back to Top](#table-of-contents)

## Static Site Hosting & CDN

Hosting for static websites, JAMstack apps, and content delivery networks for fast global asset distribution.

### [GitHub Pages](https://pages.github.com) — 🟢 Free

Free static site hosting directly from a GitHub repository, supports custom domains and Jekyll builds.

- **Free tier:** Unlimited public repos, 1GB site size soft limit, 100GB/month soft bandwidth limit.
- **Tags:** `static-hosting` `jekyll` `github`
- *Last verified: 2026-06-01*

### [Cloudflare Pages](https://pages.cloudflare.com) — 🟢 Free

Static site and full-stack hosting on Cloudflare's edge network with unlimited bandwidth.

- **Free tier:** 500 builds/month, unlimited bandwidth, unlimited sites, 100 custom domains.
- **Tags:** `static-hosting` `jamstack` `edge`
- *Last verified: 2026-06-01*

### [Surge.sh](https://surge.sh) — 🔵 Freemium

Command-line static web publishing tool — deploy a folder to a live URL in seconds.

- **Free tier:** Unlimited free deployments to *.surge.sh subdomains.
- **Paid from:** Pro adds custom domains and team features.
- **Tags:** `static-hosting` `cli` `quick-deploy`
- *Last verified: 2026-04-01*

### [Firebase Hosting](https://firebase.google.com/products/hosting) — 🔵 Freemium

Fast, secure static and SSR hosting backed by Google's CDN, integrates with the rest of the Firebase suite.

- **Free tier:** 10GB storage, 360MB/day data transfer free.
- **Paid from:** Pay-as-you-go on Blaze plan beyond free quota.
- **Tags:** `static-hosting` `google` `ssr`
- *Last verified: 2026-05-01*

### [jsDelivr](https://www.jsdelivr.com) — 🟢 Free

Free, fast CDN for npm, GitHub, and WordPress assets — widely used to serve JS/CSS libraries.

- **Free tier:** Unlimited free use for open-source/public package delivery.
- **Tags:** `cdn` `npm` `javascript`
- *Last verified: 2026-04-01*

### [raw.githack.com](https://raw.githack.com) — 🟢 Free

Serves raw files directly from GitHub/GitLab repos with correct Content-Type headers, backed by Cloudflare.

- **Free tier:** Free, unlimited use for public repo files.
- **Tags:** `cdn` `github` `raw-files`
- *Last verified: 2026-03-01*

### [Statically](https://www.statically.io) — 🟢 Free

CDN for Git repos (GitHub, GitLab, Bitbucket) plus WordPress asset and image optimization delivery.

- **Free tier:** Free CDN delivery with image transformation features.
- **Tags:** `cdn` `wordpress` `image-optimization`
- *Last verified: 2026-03-01*

### [Bunny CDN](https://bunny.net) — 🔵 Freemium

Affordable, low-latency CDN with edge storage and video streaming add-ons.

- **Free tier:** No perpetual free tier, but extremely low pay-as-you-go pricing from $0.01/GB.
- **Paid from:** From $0.01/GB bandwidth.
- **Tags:** `cdn` `video-streaming` `low-cost`
- *Last verified: 2026-04-01*

### [Fastly](https://www.fastly.com) — 🔵 Freemium

Enterprise-grade edge cloud platform and CDN with programmable edge logic (Compute@Edge).

- **Free tier:** Free usage tier covers most small projects (free up to a monthly spend threshold).
- **Paid from:** Pay-as-you-go beyond free usage allowance.
- **Tags:** `cdn` `edge-compute` `enterprise`
- *Last verified: 2026-04-01*

### [Render Static Sites](https://render.com/docs/static-sites) — 🟢 Free

Free static site hosting with global CDN, automatic HTTPS, and Git-based deploys.

- **Free tier:** Unlimited free static sites with unlimited bandwidth.
- **Tags:** `static-hosting` `cdn` `git-deploy`
- *Last verified: 2026-05-01*

[⬆️ Back to Top](#table-of-contents)

## Testing & QA

Automated browser testing, load testing, visual regression, and cross-browser/device testing platforms.

### [BrowserStack](https://www.browserstack.com) — 🔵 Freemium

Real-device and browser cloud for manual and automated cross-browser/cross-device testing.

- **Free tier:** Free trial available; open-source projects can apply for free ongoing access.
- **Paid from:** Automate plan from $39/month (annual).
- **Tags:** `cross-browser-testing` `real-devices` `automation`
- *Last verified: 2026-05-01*

### [Sauce Labs](https://saucelabs.com) — 🔵 Freemium

Cloud-based platform for automated and live testing across browsers, OSs, and real mobile devices.

- **Free tier:** Open Sauce program offers free access for qualifying open-source projects.
- **Paid from:** Virtual Cloud plan billed by usage/minutes.
- **Tags:** `cross-browser-testing` `mobile-testing` `automation`
- *Last verified: 2026-04-01*

### [Playwright](https://playwright.dev) — 🟣 Open Source

Microsoft's open-source end-to-end testing framework supporting Chromium, Firefox, and WebKit.

- **Free tier:** Completely free and open source.
- **Tags:** `e2e-testing` `open-source` `browser-automation`
- *Last verified: 2026-05-01*

### [Cypress](https://www.cypress.io) — 🔵 Freemium

JavaScript end-to-end testing framework with a real-time test runner; Cypress Cloud adds dashboards and parallelization.

- **Free tier:** Cypress test runner is free/open source; Cypress Cloud free tier includes limited test results recording.
- **Paid from:** Team plan from $75/month.
- **Tags:** `e2e-testing` `open-source` `test-dashboard`
- *Last verified: 2026-05-01*

### [k6 (Grafana)](https://k6.io) — 🔵 Freemium

Open-source load testing tool with a developer-friendly scripting API; Grafana Cloud k6 adds managed test execution.

- **Free tier:** CLI tool fully free and open source; Cloud k6 has limited free virtual user hours/month.
- **Paid from:** Cloud plans billed by virtual user hours.
- **Tags:** `load-testing` `open-source` `performance-testing`
- *Last verified: 2026-04-01*

### [Postman](https://www.postman.com) — 🔵 Freemium

API client and testing platform for building, testing, and documenting REST/GraphQL/gRPC APIs.

- **Free tier:** Free for up to 3 users with core collection/testing features.
- **Paid from:** Basic plan from $14/user/month.
- **Tags:** `api-testing` `api-client` `documentation`
- *Last verified: 2026-05-01*

### [Percy (BrowserStack)](https://www.browserstack.com/percy) — 🔵 Freemium

Visual regression testing tool that screenshots UI states and flags pixel-level diffs across builds.

- **Free tier:** Free tier with limited monthly screenshots.
- **Paid from:** Paid plans billed per screenshot volume.
- **Tags:** `visual-regression` `screenshot-testing`
- *Last verified: 2026-03-01*

### [Loader.io](https://loader.io) — 🔵 Freemium

Cloud-based load testing service from SendGrid for stress-testing APIs and websites.

- **Free tier:** Free plan with limited concurrent clients and test runs.
- **Paid from:** Paid plans increase concurrent client limits.
- **Tags:** `load-testing` `stress-testing`
- *Last verified: 2026-03-01*

### [TestRail](https://www.testrail.com) — 🔵 Freemium

Test case management platform for organizing, tracking, and reporting on manual and automated test runs.

- **Free tier:** Free tier for small teams (limited users).
- **Paid from:** Professional plan billed per user/month.
- **Tags:** `test-case-management` `qa`
- *Last verified: 2026-03-01*

[⬆️ Back to Top](#table-of-contents)

## Video, Voice & Real-Time Communication

Video conferencing SDKs, WebRTC infrastructure, live streaming, and real-time chat infrastructure for building communication features into apps.

### [Daily.co](https://www.daily.co) — 🔵 Freemium

WebRTC video/audio API for embedding live calls into apps, with prebuilt UI or fully custom SDKs.

- **Free tier:** 10,000 free participant-minutes/month.
- **Paid from:** Pay-as-you-go pricing beyond free minutes.
- **Tags:** `webrtc` `video-calling` `api`
- *Last verified: 2026-05-01*

### [Twilio Video](https://www.twilio.com/video) — 🔵 Freemium

Programmable video API for building group or 1:1 video experiences, part of the broader Twilio platform.

- **Free tier:** Free trial credit for new accounts.
- **Paid from:** Pay-as-you-go per participant-minute.
- **Tags:** `webrtc` `video-calling` `api`
- *Last verified: 2026-04-01*

### [Agora](https://www.agora.io) — 🔵 Freemium

Real-time engagement platform (voice, video, live streaming, chat) used widely in social and gaming apps.

- **Free tier:** 10,000 free minutes/month across most use cases.
- **Paid from:** Pay-as-you-go beyond free minutes.
- **Tags:** `webrtc` `live-streaming` `voice` `gaming`
- *Last verified: 2026-05-01*

### [Stream (GetStream.io)](https://getstream.io) — 🔵 Freemium

Chat and activity feed APIs/SDKs for building in-app messaging and social feeds quickly.

- **Free tier:** Free tier for small projects (limited monthly active users).
- **Paid from:** Paid plans billed per MAU beyond free tier.
- **Tags:** `chat` `activity-feeds` `messaging-sdk`
- *Last verified: 2026-04-01*

### [PubNub](https://www.pubnub.com) — 🔵 Freemium

Real-time messaging infrastructure (pub/sub) for chat, IoT, and live data sync use cases.

- **Free tier:** Free tier with 200 monthly active users included.
- **Paid from:** Paid plans billed per MAU beyond free tier.
- **Tags:** `pub-sub` `real-time-messaging` `iot`
- *Last verified: 2026-04-01*

### [Mux](https://www.mux.com) — 🔵 Freemium

Video API for encoding, storing, and streaming on-demand and live video at scale.

- **Free tier:** Small free credit for new accounts; ongoing usage is metered.
- **Paid from:** Pay-as-you-go per minute encoded/streamed.
- **Tags:** `video-streaming` `video-encoding` `api`
- *Last verified: 2026-04-01*

### [Jitsi Meet](https://jitsi.org) — 🟣 Open Source

Open-source video conferencing platform; self-host for free or use the public meet.jit.si instance.

- **Free tier:** Completely free self-hosted; public instance free with no account required.
- **Tags:** `video-conferencing` `open-source` `self-hosted`
- *Last verified: 2026-04-01*

### [LiveKit](https://livekit.io) — 🔵 Freemium

Open-source WebRTC infrastructure (SFU) for building real-time video/audio/data apps, self-hostable or managed Cloud.

- **Free tier:** Self-hosted fully free; LiveKit Cloud free tier includes limited monthly participant-minutes.
- **Paid from:** Cloud Scale plan billed on usage.
- **Tags:** `webrtc` `open-source` `self-hosted` `sfu`
- *Last verified: 2026-05-01*

[⬆️ Back to Top](#table-of-contents)


---

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

*Generated on 2026-06-28 from 31 category files, 297 entries.
Do not hand-edit this file — edit `data/categories/*.json` and run `scripts/generate_readme.py`.*
