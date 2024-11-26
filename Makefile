.PHONY: docs
docs:
	sphinx-apidoc -o docs/source ./exo/
	cd docs && make html
