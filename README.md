# Project ARGUS — River Shoals HOA Security Modernization

Welcome to the ARGUS repository: a board-owned, low-cost, defensible security and access-control modernization project for River Shoals HOA. This README is an extensive single-page overview intended to give non-technical and technical readers a clear picture of scope, design, status, and where to find more detail.

---

## At a glance

- Project: ARGUS — modernize clubhouse, pool, and gate security with a UniFi-based solution and on-premises recording.
- Community: River Shoals HOA (~440 homes)
- Goal: Replace an expensive third-party managed service with a board-owned, maintainable solution that reduces long-term costs while preserving resident access and privacy.
- Estimated capital budget (Phase 1..3): ~ $8.3k (taxed ≈ $8.9k)
- Hosting for public project materials: GitHub Pages — https://howarddalerapp.github.io/ARGUS/

---

## What this repository contains

- Root markdowns (human-editable source):
  - `ARGUS_Project_Plan.md` — Executive summary, phases, schedule, ROI.
  - `ARGUS_Network_Architecture.md` — Full network diagrams and operational-sensitive details (authorized copy also available under `docs/assets/`).
  - `ARGUS_Security_Plan.md` — Defense-in-depth, policies and operational notes.
  - `ARGUS_Operations_Guide.md` — Plain-language how-to for GHS (operators) and board members.
  - `ARGUS_Tracker.md` — Budget, procurement list and open items tracker.
  - `ARGUS_Transition_Plan.md` — CPS → ARGUS cutover plan.

- Site and published content (`docs/`): the GitHub Pages site lives here and is the recommended read for non-technical stakeholders.
  - `docs/index.html`, `docs/design.html`, `docs/security.html`, `docs/network.html`, `docs/ops.html`, `docs/tracker.html`, `docs/transition.html` — polished public pages.
  - `docs/authorized/` — gated pages intended for authorized personnel; these pages prefer pre-rendered diagrams (SVGs) and contain sensitive material.
  - `docs/assets/` — images, logos, hero SVG and extracted mermaid `.mmd` files.

- Tools and automation:
  - `tools/build_search_index.py` — regenerates `docs/search_index.json` used by the client-side search UI.
  - `tools/render_mermaid.py` — extracts mermaid code blocks to `.mmd` files; can render SVGs (local rendering requires Node/npm mermaid-cli or use the CI workflow).
  - `.github/workflows/` — GitHub Actions workflows: search index builder, manual-mermaid rendering, and other automation.

---

## Why two areas: public vs authorized

We intentionally keep most content friendly and high-level on the public pages so community members can read a short, clear description of the project. Operational-sensitive network and configuration details are preserved under the `docs/authorized/` area and `docs/assets/ARGUS_Network_Architecture.md`. The authorized area is client-side gated for convenience only — it is not a substitute for proper authenticated hosting or a VPN.

If you need full diagrams or configuration details, request access from the project owner (Howard Rapp) and we will provide secure delivery.

---

## Quick links (GitHub Pages)

- Public site root: https://howarddalerapp.github.io/ARGUS/
- Project overview (public): https://howarddalerapp.github.io/ARGUS/design.html
- Network architecture (public summary): https://howarddalerapp.github.io/ARGUS/network.html
- Authorized docs landing: https://howarddalerapp.github.io/ARGUS/authorized/index.html

Legacy links under `/ARGUS/docs/...` are supported by small redirect shim pages in `docs/docs/` to preserve older bookmarks.

---

## Developer & maintainer notes

1. Regenerate the client-side search index

   - The site uses a small client-side full-text index at `docs/search_index.json`.
   - To rebuild locally:

   ```bash
   # requires Python 3
   python3 tools/build_search_index.py --out docs/search_index.json
   ```

   - There is a GitHub Actions workflow that can run this automatically when needed.

2. Mermaid diagram rendering

   - The repo extracts mermaid diagrams into `docs/assets/mermaid/*.mmd` using `tools/render_mermaid.py`.
   - Local SVG rendering requires a mermaid CLI (for example `@mermaid-js/mermaid-cli`) and a working Node/npm toolchain. Because npm can prompt during installs, CI rendering is recommended for repeatable, non-interactive builds.

   - Recommended flow (CI): dispatch the `render-mermaid` GitHub Actions workflow from the Actions tab — it will install the renderer in the runner, render SVGs, and commit them back to `main`.

   - If you want to try locally (macOS/Linux):

   ```bash
   # install renderer once (may prompt)
   npm install -g @mermaid-js/mermaid-cli

   # extract .mmd files (this always writes the mmd files)
   python3 tools/render_mermaid.py

   # render to SVG (if mermaid-cli is installed)
   mmdc -i docs/assets/mermaid/diagram-1.mmd -o docs/assets/mermaid/diagram-1.svg
   ```

3. CI notes and Node.js 24 opt-in

   - Workflows in `.github/workflows/` were opted into Node.js 24 to avoid runner deprecation issues.
   - If a workflow fails due to node/npm versions, check the run logs for `node -v` and `npm -v` steps added for quick debugging.

---

## How to review the site locally

The site is plain static HTML; you can preview it locally with any static server. Example (python):

```bash
# from repo root
python3 -m http.server --directory docs 8000
# then open http://localhost:8000 in your browser
```

Note: Pages on GitHub will serve from `/ARGUS/` site root. Links in the site are absolute and expect that route when hosted on GitHub Pages; local preview at `/` may require adjusting paths or using a small HTML-aware server that rewrites base paths.

---

## Repo structure (high-level)

- ARGUS_Project_Plan.md — executive plan
- ARGUS_Network_Architecture.md — technical diagrams (sensitive)
- ARGUS_Security_Plan.md — security summary
- ARGUS_Operations_Guide.md — operator how-to
- tools/ — scripts for search index and mermaid extraction
- docs/ — published GitHub Pages content (site root)

---

## Contributing

- Use branches and open pull requests for non-trivial changes.
- For content edits that require review (policy, network changes), mark PRs with `needs-review` and tag project maintainers.
- If you edit diagrams or mermaid sources, run `tools/render_mermaid.py` to extract `.mmd` files and either run local rendering or dispatch the CI renderer workflow so committed SVGs remain in-sync.

---

## Legal / privacy notes

This repository contains summaries of security architecture and operational procedures. Any operational-sensitive details (IP addressing, cable routing, device configuration) are considered internal and should not be published outside the authorized channels. This repo intentionally keeps the public pages high-level.

---

If you want a shorter one-page handout or a printable board packet, I can generate a tailored PDF export from the key markdown files — tell me the audience and I'll prepare it.

---

Project owner: Howard Rapp
ARGUS
=====

Clear, friendly landing page for the ARGUS project. This repository holds planning, security, network, operations and transition docs.

Quick links
-----------

- ARGUS Project Plan — `ARGUS_Project_Plan.md`
- ARGUS Operations Guide — `ARGUS_Operations_Guide.md`
- ARGUS Network Architecture — `ARGUS_Network_Architecture.md`
- ARGUS Security Plan — `ARGUS_Security_Plan.md`
- ARGUS Tracker — `ARGUS_Tracker.md`
- ARGUS Transition Plan — `ARGUS_Transition_Plan.md`
- ARGUS Decisions Log — `ARGUS_Decisions_Log.docx`

View on the web
---------------

This repo includes a simple GitHub Pages site (published from the `docs/` folder). Once you push this repo to GitHub and enable Pages from the `main` branch (`/docs` folder), the project landing page will be available at: `https://<your-username>.github.io/<repo-name>/`.

How I prepared the repo
-----------------------

- Added a small, attractive `docs/index.html` so non-technical people get a clean landing page.
- Added `.nojekyll` so the `docs/` HTML renders correctly.
- Added a minimal `.gitignore` and this `README.md`.

Next steps (pick one)
---------------------

1. Create a GitHub repository (or tell me the remote URL) and I will add it and push the initial commit.
2. I can create the GitHub repo for you if you provide the GitHub account and give permission (or provide a personal access token). I won't do this without your OK.

Commands you'll run (replace placeholders):

Add a remote and push:

    git remote add origin git@github.com:<your-username>/<repo-name>.git
    git push -u origin main

Or with HTTPS:

    git remote add origin https://github.com/<your-username>/<repo-name>.git
    git push -u origin main

Enable Pages on GitHub
----------------------

1. Go to the repo Settings → Pages.
2. Source: select Branch: `main`, folder: `/docs` and Save.

Want me to do it for you? Tell me:

- The GitHub repo name you prefer (if different from this folder name).
- Whether you want me to create the repo under your account.
- Whether to convert Word docs (`.docx`) to Markdown and include them.

Status: I inspected the repo — there are local files and no remotes yet. I added a simple landing page in `docs/` and committed it locally so you're ready to push.
