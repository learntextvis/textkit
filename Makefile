
test:
	py.test

lint:
	pylint --rcfile .pylint textkit/*/**.py

install_dev:
	pip install --editable .

package:
	python setup.py egg_info
	python setup.py sdist
	python setup.py bdist_wheel --universal

publish:package
	twine upload dist/*

clean:
	rm -rf build
	rm -rf textkit.egg-info
	rm -rf dist
