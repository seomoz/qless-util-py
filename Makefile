all: test

.PHONY: clean
clean:
	# Remove the build
	rm -rf build dist
	# And all of our pyc files
	find . -name '*.pyc' -delete
	# And lastly, .coverage files
	find . -name .coverage -delete

requirements:
	pip freeze | grep -v -e qless-util > requirements.txt

.PHONY: test
test:
	nosetests --with-coverage
