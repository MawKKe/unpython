# unpython

Un-pythons a python subprocess command+arguments list back into CLI-friendly form.

Python scripts that deal with `subprocess` module usually need to prepare a list
of string arguments for use with `subprocess.run()` (or similar). Sometimes
you need to perform some quick n' dirty `print()` debugging to inspect the contents
of that list. Or you may observe such lists being printed in production system
logs. Any case, you might want to run the underlying command manually to verify
whether it works as expected. But now you have to somehow "peel off" the pythonic
list notation so that you can run the underlying command in a terminal.

You might get away doing the massaging by hand, although that becomes _really_
annoying _really_ fast. And it is also very error prone; you need to know how
to handle spaces and quotation correctly. Not fun.

You could, of course, use the built-in `shlex` module to convert the list into
CLI-safe form before printing.  That's what this tool does too. However,
sometimes the code that does the printing might be outside of your control...

Alternatively, you can use this tool for doing the conversion for you automatically.
You only need to copy-paste the command list into the interactive prompt, and you
will receive a valid, CLI-friendly command string in return :)

As you might notice, the functionality of this tool is rather simple; the goal
of this repo is to provide the functionality in an easily installable package
(especially if you use `pipx`).

# Install

    $ pip install --user git+https://github.com/MawKKe/unpython

I recommend using `pipx`:

    $ pipx install git+https://github.com/MawKKe/unpython

just make sure that pipx is configured correctly (i.e. installed programs are
available in your `$PATH`).

# Usage

Run the program , then copy-paste your python list object into the
prompt:

    $ unpython
    ...
    >>> ['ls', '-l', 'foo/bar with spaces']


now it should print

    ls -l 'foo/bar with spaces'

You can then copy this output into a terminal to run your command the usual
way. The `unpython` *should* handle quotation etc. correctly for you.


# License

Copyright 2024 Markus Holmström (MawKKe)

The works under this repository are licenced under Apache License 2.0.
See file `LICENSE` for more information.

# Contributing

This project is hosted at https://github.com/MawKKe/unpython

You are welcome to leave bug reports, fixes and feature requests. Thanks!

