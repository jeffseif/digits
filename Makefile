.PHONY: all clean install test train

all: install train

install: venv/.setup
	@true

venv/.setup: venv
	@$</bin/python setup.py \
		install \
		--quiet
	@touch $@

venv: requirements.txt
	@virtualenv \
		--no-site-packages \
		--python=$(which python3) \
		$@
	@$@/bin/pip install \
		--requirement $<
	@touch $@

train: model.pkl

model.pkl: venv corpus
	@$</bin/python -m digits.main \
		train \
		--model-filename=$@ \
		--validate
	@touch $@

corpus:
	@mkdir -p $@
	@./scripts/get_corpus.sh
	@touch $@

test: venv
	@$</bin/tox

clean:
	venv/bin/python setup.py clean --all
	rm -rf *.egg-info/
	rm -rf .cache/
	rm -rf .eggs/
	rm -rf .tox/
	rm -rf dist/
	rm -f .coverage
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -delete
