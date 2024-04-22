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
import ast

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

NOTE: the expression must be a list and only contain string literals
""".strip()
    )
    print()
    print('-' * 5)
    print('Enter python list to un-python:')
    expr = input('>>> ')
    print('-' * 5)
    print()

    try:
        li = ast.literal_eval(expr)
        if not isinstance(li, (list, tuple)):
            print('ERROR: expression is not a list')
            return 10
        for i, e in enumerate(li):
            if not isinstance(e, str):
                print(f'ERROR: element "{e}" at index #{i} is not a string literal')
                return 20
        print('#', shlex.join(str(o) for o in li))
    except ValueError as e:
        print('ERROR: list contains non-literal expressions')
        return 30

    return 0

if __name__ == '__main__':
    sys.exit(main())
