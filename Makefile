# Developer shortcuts for Trinity Hub. Run `make help` for a summary.

PYTHON ?= python3
PORT   ?= 8000

.PHONY: help preview build regen validate linkcheck

help:  ## Show this help
	@grep -E '^[a-z][a-zA-Z_-]*:.*## ' $(MAKEFILE_LIST) | awk -F ':.*## ' '{printf "  make %-10s %s\n", $$1, $$2}'

preview:  ## Live-reload docs preview, no network needed (skips social cards)
	SOCIAL_CARDS=false mkdocs serve -a localhost:$(PORT)

build:  ## Strict production build into site/ (social cards need network + cairo)
	mkdocs build --strict

regen:  ## Regenerate all generated artifacts from their sources
	$(PYTHON) scripts/build_index.py
	$(PYTHON) scripts/build_registry_page.py
	$(PYTHON) scripts/build_campaign_index.py
	$(PYTHON) scripts/build_whats_new_feed.py

linkcheck:  ## Build offline and check every internal link and anchor
	SOCIAL_CARDS=false mkdocs build --strict -d .linkcheck-site
	$(PYTHON) scripts/check_links.py .linkcheck-site
	rm -rf .linkcheck-site

validate:  ## What CI checks: registry schemas + generated files are committed fresh
	$(PYTHON) scripts/validate_registry.py
	$(PYTHON) scripts/build_index.py
	git diff --exit-code -- registry/INDEX.md
	$(PYTHON) scripts/build_registry_page.py
	git diff --exit-code -- docs/registry/index.md
