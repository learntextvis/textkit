.. _contributing:

Contributing
============

If you are interested in contributing to textkit we would love your help!

Here is a bit more about the structure of the codebase and how to contribute.

Code Structure
--------------

Each command is implemented in its own file. These command files are organized into
sub-directories:

* tokenize
* filter
* transform
* stats
* package

The use of these sub-directories is primarily for developer convenience and commands
can be moved around if a better structure is found.

Commands
--------

textkit uses `Click <http://click.pocoo.org/>`_. to handle command line arguments
and inputs. Click uses decorators to define these arguments and options in a succinct way.

textkit strives to use text as an input and text as an output. Raw text can be processed
using commands that start with ``text2`` like ``text2words``.

Token documents (text files with a token on each line) can be used and produced by
commands that include ``words`` in the name.

Utilities
---------

There are a very small set of utility functions that are useful in keeping textkit

These are contained in the ``utils.py`` file. Some that you might find helpful:

``read_tokens`` will convert a token document into a list of tokens. Use this to process the
input file if your input is a token document.

``output`` is a light wrapper around the output capabilities of Click that prevents
error messages if the command is exited early (like when piping to ``head``).

Writing New Commands
--------------------

Want to contribute a new command? Great!

textkit uses GitHub Pull Requests to incorporate other developer's work.

Fork the repo and then create a branch for your new command. Create and test it,
then submit a Pull Request. 
