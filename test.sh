#!/usr/bin/env bash
set -euo pipefail

echo "Testing gutentag-world-http..."

grep -rq "Gutentag, World!" --include="*.py" --include="*.ts" --include="*.js" --include="*.html" --include="*.yaml" --include="*.yml" --include="*.json" --include="*.tf" --include="*.toml" --include="*.ino" --include="*.proto" --include="*.sql" --include="*.rb" --include="*.ex" --include="*.go" --include="*.rs" --include="*.swift" --include="*.java" --include="*.cs" --include="*.lol" --include="*.rock" --include="*.spl" --include="*.emojic" --include="*.tex" --include="*.redis" --include="*.wat" --include="*.cron" . || grep -rq "Gutentag, World!" .

echo "PASS"
