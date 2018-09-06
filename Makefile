
all:

unittest:
	nosetests -s

test-basic:
	./single.py -c sleep 5 &
	sleep 0.3
	./single.py -c sleep 3; true

register:
	python setup.py register sdist upload

dist:
	python setup.py sdist
