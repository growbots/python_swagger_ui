package:
	python setup.py sdist bdist_wheel

upload:
	python setup.py sdist bdist_wheel upload

clean:
	rm -rv .cache .coverage build dist *.egg-info .eggs .tox
