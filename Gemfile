source "https://rubygems.org"

# GitHub Pages manages the compatible Jekyll version.
# Run with:
#
#   bundle exec jekyll serve
#
gem "github-pages", group: :jekyll_plugins

# Default theme dependency
gem "minima", "~> 2.5"

# Jekyll plugins
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
end

# Windows and JRuby do not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance booster for Windows
gem "wdm", "~> 0.1", platforms: [:mingw, :x64_mingw, :mswin]

# Lock http_parser.rb for JRuby compatibility
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]