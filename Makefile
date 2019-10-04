clean:
	rm -rf build
	rm -rf *.egg-info
	rm -rf dist

build: clean
	python3 setup.py sdist bdist_wheel --universal
	gpg --detach-sign -a dist/*

upload:
	python3 -m twine upload  dist/*
