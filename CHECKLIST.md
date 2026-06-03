# Release validation

Before opening a PR, publishing the marketplace, or filming an install:

**Claude Code install check:** after `/plugin install <name>@claude-for-hk-law`, run `/reload-plugins` (full restart only if skills do not appear in `/` autocomplete).

Validation:

```bash
claude plugin validate .claude-plugin/marketplace.json
for d in commercial-legal privacy-legal employment-legal ip-legal corporate-legal litigation-legal \
  product-legal regulatory-legal ai-governance-legal law-student legal-clinic legal-builder-hub \
  hk-property hk-arbitration hk-commercial-law hk-competition hk-immigration hk-shipping-maritime \
  hk-family-law hk-trusts-estate hk-basic-law; do
  [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"
done
python3 scripts/lint-tool-scope.py
bash scripts/test-cookbooks.sh
```

Sanity checks:

- No `claude-for-legal` config paths remain: `grep -r claude-for-legal .`
- Removed plugins are gone from marketplace: `hk-data-privacy`, `hk-employment`, `hk-companies`, `hk-litigation-procedure`, `hk-intellectual-property`, `hk-nsl-rules`
