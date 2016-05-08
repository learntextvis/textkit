.. _install:

Installation
============

Using pip
+++++++++

Most users should be able to install textkit easily using pip:

``pip install -U textkit``

To ensure you have all the data files needed to run all the commands, you should then run:

``textkit download``

This will download some files that NLTK (a dependency of textkit) needs for certain commands.

From Source
+++++++++++

Textkit is developed and maintained on github, so building from source is also easy.

First clone the repo:

``git clone git@github.com:learntextvis/textkit.git``

Then navigate to the `textkit` directory to install its requirements

.. doctest::

     cd textkit
     pip install -r requirements.txt

Finally, install the local version of textkit using the `--editable` flag:

.. doctest::

     pip install --editable .
