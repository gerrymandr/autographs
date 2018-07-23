
setup:
	pip install -r requirements.txt
	python setup.py develop

build:
	python setup.py sdist
	python setup.py bdist_wheel

upload:
	twine upload dist/*
