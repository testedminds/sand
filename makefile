SHELL = /usr/bin/env bash

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

publish:
	python setup.py sdist bdist_wheel
	gpg --detach-sign -a dist/*.tar.gz
	#twine upload dist/*.tar.gz *.tar.gz.asc
	#rm -rf build dist .egg sand.egg-info
