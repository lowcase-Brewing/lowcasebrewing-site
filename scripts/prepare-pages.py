"""Copy the static site and prefix root-relative HTML URLs for Pages project sites."""
import argparse
import re
import shutil
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base-path', default='')
parser.add_argument('--output', type=Path, default=Path('_pages'))
args = parser.parse_args()
base = '/' + args.base_path.strip('/') if args.base_path.strip('/') else ''
if not re.fullmatch(r'(?:/[A-Za-z0-9_.-]+)*', base):
    parser.error('base path must contain only URL-safe path segments')
source = Path('dist').resolve()
output = args.output.resolve()
if output == source or source in output.parents or output in source.parents:
    parser.error('output must be separate from the source folder')
output.mkdir(parents=True, exist_ok=False)
shutil.copytree(source, output, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.DS_Store'))
if base:
    for page in output.rglob('*.html'):
        text = page.read_text()
        text = re.sub(r'((?:href|src)\s*=\s*[\"\x27])/(?!/)',
                      lambda match: match.group(1) + base + '/', text)
        page.write_text(text)
(output / '.nojekyll').touch()
print(f'Prepared {output} with base path {base or "/"}')
