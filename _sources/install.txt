.. _install:

Installation
============

To test locally, clone the repo:

``git clone git@github.com:learntextvis/textkit.git``

Create a local virtual environment or `conda` environment.

Here is how I created my local `conda` environment for installing and testing textkit:

.. doctest::

     conda create -name textkit nltk
     source activate textkit

Then I went into the `textkit` directory to install its requirements

.. doctest::

     cd textkit
     pip install -r requirements.txt

Finally, I installed the local version of textkit using the `--editable` flag:

.. doctest::

     pip install --editable .

_In the future basic installation instructions will be just the following:_

textkit is available via `pip`:

.. doctest::

     pip install textkit

Dependencies
++++++++++++

Textkit depends on NLTK 3. NLTK will be installed automatically when you run ``pip install textkit`` or ``python setup.py install``.
