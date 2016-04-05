.. _quickstart:

Tutorial: Quickstart
====================

 .. module:: textkit.cli

Convert Text to Tokens
------------------------

Tokenization is the process of turning text into chunks of text.
These chunks can be sentences, words, or even sections of words.

Textkit converts a text file into a **token document** - where each line has one token per line.

Here, we convert a text file into a token document where each token is a word.

.. doctest::

    textkit text2words input.txt

Output goes to standard out. You can redirect with ``>``.

.. doctest::

    textkit text2words input.txt > words.txt

We can also get **bigrams** (two word tokens).

.. doctest::

    textkit text2words input.txt | textkit words2bigrams > bigrams.txt

Here we first convert the text to word tokens and use that as the input for the bigram tokenization.

Note the use of **|** for piping one textkit command into another.

With no file passed in, many textkit commands default to standard in.
This can be indicated explicitly by using a dash (`-`) to indicate standard in.

Any command that uses ``words`` expects to work with **token documents** that have one word per line.

Filter and Transform
--------------------

Once you have your text tokenized, you can filter out tokens you might not want in your document.

Let's remove punctuation from the ``words.txt`` file.

.. doctest::

    textkit filterpunc words.txt

We can also transform the tokens in various ways, such as through lowercasing everything:

.. doctest::

    textkit lowercaser words.txt

Package
-------

Once the tokens are setup and transformed the way you want them,
it can be useful to package up a set of documents into a single file for downstream visualization or other uses.

.. doctest::

    textkit tokens2json words1.txt words2.txt > out.json
