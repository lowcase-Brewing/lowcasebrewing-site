# lowcase Brewing — complete source

The existing static website, with its design and content preserved.

## Continue in another chat

Upload this ZIP and ask:

"Save these existing working files to the lowcase Brewing Sites project and publish it. Use project ID appgprj_6abc3d06a3b48191b65bd3dc5fe047ce. Preserve the existing design. Reuse the existing project; do not create a new site. Preserve its public access."

## Continue on a different computer

Log into ChatGPT with as the user who owns the lowcase Brewing site and ask:

"Continue maintaining my existing lowcase Brewing Site, project ID appgprj_6abc3d06a3b48191b65bd3dc5fe047ce.
Retrieve its latest source before editing. Preserve its design, domains, Google Analytics, and public access.
Update this existing project rather than creating a new Site."

## Included files

- .openai/hosting.json — Sites project identity, when present in a Sites checkout; not needed for GitHub Pages
- dist/index.html — complete page content
- dist/style.css — complete styling and responsive layouts
- dist/journal.js — category filters and article dialogs
- dist/assets/ — logos, beer labels, and generated photography

This is a buildless static site. No dependency installation or build is required. Open dist/index.html to view it locally, or serve the dist folder with a local web server.

The site is currently published through Sites. This repository prepares an independent GitHub Pages deployment for testing.

No credentials or tokens are included. Obtain a fresh source-repository credential for the existing project through Sites.

Content includes real lowcase brew stories and external AHA recipe links.

## GitHub Pages test deployment

In this repository's Settings > Pages, select **GitHub Actions** as the source.
Leave the custom domain unset while testing; leave Namecheap DNS pointing to Sites.
The workflow publishes `dist/` after copying it into a temporary `_pages/` folder.
GitHub's reported base path is added to root-relative links in that copy, so both
project URLs and a future custom domain work without changing the authored pages.

Push the reviewed changes to `main`, then inspect the Pages workflow in Actions.
The resulting test URL is reported by the deployment; verify navigation, all four
beer pages, notebook filters/dialogs, labels, and the favicon before changing DNS.
If the account's main GitHub Pages site still has a custom domain, it can affect
project-site URLs; clear that old association or use a dedicated test subdomain.

Local checks (use a fresh output directory for each run):

```sh
python3 scripts/prepare-pages.py --base-path /lowcasebrewing-site --output /tmp/lowcase-pages-test
python3 -m http.server 8000 --directory dist
```

The local server previews source at the URL root. The deployment prepares paths
for the actual Pages URL. No npm installation or Jekyll build is needed.
