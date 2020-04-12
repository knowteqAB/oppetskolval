.PHONY: help prepare-dev test lint doc

.DEFAULT: help

help:
	@echo "make prepare-dev"
	@echo "      prepare development environment. This will install oppetskolval in development mode by pip."
	@echo "make test"
	@echo "      run tests"
	@echo "make lint"
	@echo "      validate pep8 compliance"
	@echo "make doc"
	@echo "      build html doc for oppetskolval"

prepare-dev:
	pip install flake8 autopep8
	@echo "\n\e[92mInstalling 'oppetskolval' in developer mode...\e[39m"
	pip install -e .
	@echo "\n\e[92mRunning tests...\e[39m"
	pytest

test:
	pytest

lint:
	flake8 --ignore=W391,E501 src/ tests/

doc:
	pdoc -o ./doc/html --html -c latex_math=True src/oppetskolval --force
