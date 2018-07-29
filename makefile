
setup:
	pip install -r requirements.txt
	python setup.py develop

build:
	echo "Building for distribution."
	python setup.py sdist
	python setup.py bdist_wheel

upload:
	echo "Uploading to PyPi."
	twine upload dist/*

dev:
	echo "Running a dev installation to the default Python interpreter."
	/usr/bin/env python setup.py install
