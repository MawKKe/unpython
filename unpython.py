#!/usr/bin/env python3

"""
What is this?
-------------

Un-pythons a python subprocess command+arguments list back into CLI-friendly form.

Install
-------
1) Save this script into somewhere in your $PATH.
   Save the script with name 'unpython'
2) make the script runnable:
    $ chmod +x path/to/script
3) now it should be runnable:
    $ unpython

HINT: Use rlwrap to make the input() more user friendly.
      Set an alias in your shell config:

        alias unpython="rlwrap unpython"

Author: Markus H (MawKKe) <markus@mawkke.fi> 2024-04-21
"""

import sys
import shlex


def main():
    if len(sys.argv) > 1:
       print('ERROR: program is interactive and takes no arguments')
       return 1

    print(r"""
Un-pythons a python subprocess command+arguments list back into CLI-friendly form.

Example:
    >>> ['ls', '-l', 'foo/bar with spaces']
    ->
    ls -l 'foo/bar with spaces'

WARNING: the tool runs eval() on the given input
""".strip()
    )
    print()
    print('-' * 5)
    print('Enter python list to un-python:')
    arg = input('>>> ')
    print('-' * 5)
    print()

    li = eval(arg)
    print('#', shlex.join(str(o) for o in li))

    return 0

if __name__ == '__main__':
    sys.exit(main())
