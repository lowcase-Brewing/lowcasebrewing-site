# lowcase Brewing

This repo houses the static web site for lowcase Brewing (lowcasebrewing.com). The site is hosted through GitHub Pages and is deployed using GitHub Actions.

## Included files

- dist/index.html — complete page content
- dist/style.css — complete styling and responsive layouts
- dist/journal.js — category filters and article dialogs
- dist/assets/ — logos, beer labels, and generated photography

This is a static site with no application build step. No npm installation or Jekyll build is required. Use a local web server to preview it so navigation works as it does on the live site.

Content includes real lowcase brew stories and external AHA recipe links.

## GitHub Pages deployment

The live site is available at https://lowcasebrewing.com. GitHub Pages redirects
https://www.lowcasebrewing.com to that address.

The workflow in `.github/workflows/pages.yml` runs when changes are pushed to
`main`, including when a pull request is merged into `main` on GitHub. A local
commit alone does not deploy the site. You can also run the workflow manually
from the repository's Actions tab.

The workflow uses `scripts/prepare-pages.py` to copy `dist/` into a temporary
`_pages/` folder, exclude macOS metadata, and add `.nojekyll`. It uses GitHub's
reported base path to adjust root-relative links in the deployment copy when
needed. The current custom domain uses an empty base path; project URLs such as
`/lowcasebrewing-site/` use a prefix. The authored files in `dist/` stay unchanged.

Keep this script: it is part of the deployment workflow. `_pages/` is generated
output and should not be committed.

After publishing, check the workflow result in Actions and verify navigation,
beer pages, notebook filters and stories, images, and the favicon on the live site.
If the custom domain changes, run the workflow again to regenerate the site for
its new URL.

## Local preview

From the repository root, run:

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000 in your browser. Press Ctrl+C in the terminal to stop
the server. The deployment preparation script does not need to be run for a
normal local preview.
