
setup:
	pip install -r requirements.txt
	python setup.py develop

build: FORCE
	echo "Building for distribution."
	python setup.py sdist
	python setup.py bdist_wheel

FORCE:

upload:
	echo "Uploading to PyPi."
	twine upload dist/*

dev:
	echo "Running a dev installation to the default Python interpreter."
	/usr/bin/env python setup.py install
	echo "Decompressing test files."
	unzip test/data/2018_19_counties.zip -d test/data
	unzip test/data/tl_2016_19_cousub.zip -d test/data
