build:
	echo "Building for distribution."
	python setup.py sdist
	python setup.py bdist_wheel

upload:
	echo "Uploading to PyPi."
	twine upload dist/*

dev:
	ehco "Running a dev installation to the default Python interpreter."
	/usr/bin/env python setup.py install
