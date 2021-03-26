.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: requirements
requirements:
	pip-compile requirements.in && pip-sync