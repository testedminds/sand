SHELL = /usr/bin/env bash

version = `python -c "import sand; print(sand.__version__)"`
img-name = sand
name = $(img-name)-$(version)

include docker/makefile

ci: test flake8

test:
	py.test

flake8:
	flake8 --ignore=E501 sand

# https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode
requirements:
	pip install -r requirements.txt

env:
	conda create --name sand python=3.9
	conda install --force-reinstall -y -q --name sand -c conda-forge --file requirements.txt
	source ${CONDA_PREFIX}/bin/activate sand && \
	python setup.py develop

rm-env:
	conda env remove --name sand

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
	@echo "Now increment version in sand/__version__.py to start next release."
