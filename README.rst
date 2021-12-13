``SMOP`` is Small Matlab and Octave to Python compiler.
 ``SMOP`` translates matlab to python. Despite obvious similarities
 between matlab and numeric python, there are enough differences to
 make manual translation infeasible in real life.  ``SMOP`` generates
 human-readable python.

 Smop3 is the community maintained version of https://github.com/victorlei/smop/
 abandoned somewhere around 2018. SMOP is looking for maintainers and people
 with knowledge on lexers and parsers to help clean up the project!

Installation
============

``smop3`` is available from PyPI::

.. code-block:: bash

  pip install smop3

Developers can clone the GitHub repository and use editable installs::

.. code-block:: bash

  git clone git@github.com:smop3/smop
  cd smop3
  pip install -e .

Random remarks
==============

With less than five thousands lines of python code
``SMOP`` does not pretend to compete with such polished
products as matlab or octave.  Yet, it is not a toy.
There is an attempt to follow the original matlab
semantics as close as possible.  Matlab language
definition (never published afaik) is full of dark
corners, and ``SMOP`` tries to follow matlab as
precisely as possible.

There is a price, too.
The generated sources are
`matlabic`, rather than `pythonic`, which means that
library maintainers must be fluent in both languages,
and the old development environment must be kept around.

Should the generated program be `pythonic` or `matlabic`?
For example should array indexing start with zero
(`pythonic`) or with one (`matlabic`)?

I beleive now that some matlabic accent is unavoidable
in the generated python sources.  Imagine matlab program
is using regular expressions, matlab style.  We are not
going to translate them to python style, and that code
will remain forever as a reminder of the program's
matlab origin.

Another example.  Matlab code opens a file; fopen
returns -1 on error.  Pythonic code would raise
exception, but we are not going to do `that`.   Instead,
we will live with the accent, and smop takes this to the
extreme --- the matlab program remains mostly unchanged.

It turns out that generating `matlabic`` allows for
moving much of the project complexity out of the
compiler (which is already complicated enough) and into
the runtime library, where there is almost no
interaction between the library parts.

Which one is faster --- python or octave?  I don't know.
Doing reliable performance measurements is notoriously
hard, and is of low priority for me now.  Instead, I wrote
a simple driver ``go.m`` and ``go.py`` and rewrote `rand`
so that python and octave versions run the same code.
Then I ran the above example on my laptop.  The results
are twice as fast for the python version.   What does it
mean?  Probably nothing. YMMV.

Running the test suite
======================

The test suite uses Python's ``unittest`` module and can be executed with::

.. code-block:: bash

  python -m unittest

Command-line options
====================

The command line interface can be accessed using either the ``smop`` command,
or if wrappers are unavailable on your system ``python -m smop`` can be used::

.. code-block:: bash

  python -m smop

.. code-block:: bash

  SMOP compiler version 0.25.1
  Usage: smop [options] file-list
      Options:
      -V --version
      -X --exclude=FILES      Ignore files listed in comma-separated list FILES
      -d --dot=REGEX          For functions whose names match REGEX, save debugging
                              information in "dot" format (see www.graphviz.org).
                              You need an installation of graphviz to use --dot
                              option.  Use "dot" utility to create a pdf file.
                              For example:
                                  $ python main.py fastsolver.m -d "solver|cbest"
                                  $ dot -Tpdf -o resolve_solver.pdf resolve_solver.dot
      -h --help
      -o --output=FILENAME    By default create file named a.py
      -o- --output=-          Use standard output
      -s --strict             Stop on the first error
      -v --verbose
