
all:

README:
	./single.py -h > $@

test:
	nosetests -s

test-basic:
	./single.py -c sleep 5 &
	./single.py -c sleep 3

t:
	find . | ./single.py -c wc -l

tt:
	$(PWD)/single.py -c sleep 2

status:
	./single.py -s -c sleep

n:
	./single.py -s -c non-existent

h:
	./single.py -h

e:
	./test_exec.py find . | wc -l
	find . | ./test_exec.py wc -l


o:
	@#./opt_fsm.py -f x.lock wc -c Makefile
	@#./opt_fsm.py -f x.lock -c wc -c Makefile
	./opt_fsm.py -c x wc -c Makefile

p:
	./test_optparse.py -f x.lock -c wc -c Makefile

no-c:
	./single.py ls
no-arg:
	./single.py

register:
	python setup.py register sdist upload

dist:
	python setup.py sdist

test.ve:
	virtualenv --no-site-packages $@

install: test.ve
	find test.ve | sort > x.0
	. test.ve/bin/activate; python setup.py install
	find test.ve | sort > x.1
	comm -23 x.1 x.0
