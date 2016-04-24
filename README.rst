textkit
=======

Simple text analysis from the command line.

Homepage: `http://learntextvis.github.io/textkit/ <http://learntextvis.github.io/textkit/>`_

About
-----

`textkit` is a series of small, unix-style tools that provide a suite of capabilities for
dealing with text as data.

Think of textkit as basic natural language processing capabilities - from the command line.

textkit Features
----------------

Here are some of the cool things you can do with textkit.

Convert a document to a set of word tokens and remove all punctuation from the tokens:

.. code-block:: python

    textkit text2words input.txt | textkit filterpunc

Count top used words in a text:

.. code-block:: python

    textkit text2words alice.txt | textkit count --limit 20

Do the same, but with punctuation removed:

.. code-block:: python

    textkit text2words alice.txt | textkit filterpunc | textkit count --limit 20

Installation
------------
::

    $ pip install -U textkit
    $ textkit --help


Dev install
-----------

To test locally, clone the repo:

::

    git clone git@github.com:learntextvis/textkit.git


Create a local virtual environment or `conda` environment.

Here is how I created my local `conda` environment for installing and testing textkit:

::

    conda create --name textkit nltk

    source activate textkit

Then I went into the `textkit` directory to install its requirements

::

    cd textkit

    pip install -r requirements.txt

Finally, I installed the local version of textkit using the `--editable` flag:

::

    pip install --editable .

Examples
--------

See more examples at the `Quickstart guide`_.

.. _`Quickstart guide`: http://learntextvis.github.io/textkit/quickstart.html


Requirements
------------

- Python >= 2.6 or >= 3.3

Project Links
-------------

- Docs: http://learntextvis.github.io/textkit/
- PyPI: https://pypi.python.org/pypi/textkit
- Issues: https://github.com/learntextvis/textkit/issues
