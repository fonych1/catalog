.PHONY: help docs
.DEFAULT_GOAL := help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install dev requirements
	pip install -r requirements.txt

lock: ## Compile all requirements files
	pip-compile --resolver=backtracking --no-header --verbose --output-file requirements.txt requirements.in

upgrade: ## Upgrade requirements files
	pip-compile --resolver=backtracking --no-header --verbose --upgrade --output-file requirements.txt requirements.in

lint: ## Run code linters
	flake8 catalog
	mypy catalog

test: ## Run tests
	pytest
