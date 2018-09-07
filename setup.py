
from distutils.core import setup
    
setup(
    name = "single",
    version = "0.2.0",
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
    long_description = """
    Wrap a command with `single` to ensure there is at most single instance of the command at a time.
    This comes in handy when periodically invoking potentially long-running commands by cron.
    `single` avoids the problem of stale lock suffered by lock file approach. Even if the command
    crashes the lock is cleared.
    """
    )
