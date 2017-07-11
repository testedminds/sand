SHELL = /usr/bin/env bash

version = `python -c "import sand; print(sand.__version__)"`
name = sand-$(version)

ci: test flake8

test:
	py.test

flake8:
	flake8 --ignore=E501 sand

install-deps:
	pip install -r requirements.txt

# https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode
install-develop:
	pip install -e .

publish: wheel sign upload clean tag

wheel:
	python setup.py sdist bdist_wheel

sign:
	gpg --detach-sign -a dist/$(name).tar.gz
	gpg --detach-sign -a dist/$(name)-py3-none-any.whl

upload:
	twine upload dist/$(name)-py3-none-any.whl dist/$(name)-py3-none-any.whl.asc
	twine upload dist/$(name).tar.gz dist/$(name).tar.gz.asc

clean:
	rm -rf build dist .egg sand.egg-info

tag:
	git tag v$(version)
	git push --tags
