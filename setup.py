
from distutils.core import setup
    
setup(
    name = "single",
    version = "0.1.0",
    python_requires='>=2.6',
    py_modules = ["single"],
    scripts = ["single.py"],
    license = "LGPL",
    description = "Ensure single instance of a command without leaving stale lock files.",
    author = "tengu",
    author_email = "karasuyamatengu@gmail.com",
    url = "https://github.com/tengu/py-single",
    classifiers = [
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        ],
    # xx generate this from ./single.py --help
    long_description = """ A wrapper command to provide an advisory lock, without leaving stale lock files.
Usage: single.py [options] -c command args..

Options:
  -h, --help            show this help message and exit
  -f LOCK_FILE, --lock-file=LOCK_FILE
                        Path to the lock file. Default is provided based on the command path if omitted.
  -s, --status          Check to see if the file is locked, and if so, by which process. Exit status is 0
                        if unlocked, 1 if locked.

flock(2)'ed file is used to provide locking. This will not leave stale lock files around. 
Note that the existance of lock file does not mean that there is an outstanding lock; 
exclusive flock must be held by a process. 
So use 'single.py --status -f /tmp/foo.lock' to see if the lock is held. 

The OS releases the lock upon process termination, so the lock file is released 
regardless of how the job terminated.

Invocations: 

* single.py -c long-running-scrit arg1 arg2
  will ensure only one long-running-scrit will run at a time.
  Default lock file, specific to the command, is used in the absence of -f option.

* Lockfile can be explicitely specified as:
  single.py -f /tmp/lrs-foo.lock -c long-running-scrit foo
  Two jobs using the same command could be run concurrently by using different lock files, like:
  single.py -f /tmp/lrs-bar.lock -c long-running-scrit bar

* Use --status (-s) option to check if a command or a file is locked:
  single.py -s -f /tmp/foo.lock
  single.py -s -c long-running-scrit 

Example: $ single.py -c sleep 3 & for x in {0..6}; do single.py -s -c sleep; sleep 1; done
[1] 32567
locked by 32567: /tmp/single.py_bin_sleep.flock
locked by 32567: /tmp/single.py_bin_sleep.flock
locked by 32567: /tmp/single.py_bin_sleep.flock
[1]+  Done                    single.py sleep 5
not locked: /tmp/single.py_bin_sleep.flock
not locked: /tmp/single.py_bin_sleep.flock
"""
    )
