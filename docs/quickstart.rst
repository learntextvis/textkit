.. _quickstart:

Tutorial: Quickstart
====================

 .. module:: textkit.cli

 Let's say we have a very short piece of text stored in ``input.txt``. It looks something like:

 .. doctest::

    Mrs. Bennet deigned not to make any reply, but, unable to contain
    herself, began scolding one of her daughters.

What are some of the tools in textkit that we can use on this text?

Convert Text to Tokens
------------------------

Tokenization is the process of turning text into chunks of text.
These chunks can be sentences, words, or even sections of words.

Textkit converts a text file into a **token document** - where each line has one token per line.

.. doctest::

    textkit text2words input.txt

This command converts our input.txt text file into a token document where each token is a word.

The output would look something like:

.. doctest::

    Mrs.
    Bennet
    deigned
    not
    to
    make
    any
    reply
    ,
    but
    ,
    unable
    to
    contain
    herself
    ,
    began
    scolding
    one
    of
    her
    daughters
    .


This is typically the first thing we want to do when using textkit, as textkit is all about working with tokens.

The output by default goes to standard out. You can redirect to a file by using ``>``.

.. doctest::

    textkit text2words input.txt > words.txt

This would put our words into ``words.txt``.

We can also get **bigrams** (two word tokens).

.. doctest::

    textkit text2words input.txt | textkit words2bigrams > bigrams.txt

Here we first convert the text to word tokens and use that as the input for the bigram tokenization.

The contents of ``bigrams.txt`` would look like:

.. doctest::

    Mrs. Bennet
    Bennet deigned
    deigned not
    not to
    to make
    make any
    any reply
    reply ,
    , but
    but ,
    , unable
    unable to
    to contain
    contain herself
    herself ,
    , began
    began scolding
    scolding one
    one of
    of her
    her daughters
    daughters .

Note the use of **|** for piping one textkit command into another.

With no file passed in, many textkit commands default to standard in.
This can be indicated explicitly by using a dash (``-``) to indicate standard in.

Commands that begin with ``text`` in textkit transform text into tokens of some sort.

Any command that uses ``words`` expects to work with **token documents** that have one word per line.

A bigram is just a special case of an ``NGram`` - so lets make some ngrams of size 5:

.. doctest::

    textkit text2words input.txt | textkit words2ngrams -n 5

Which produces:

.. doctest::

    Mrs. Bennet deigned not to
    Bennet deigned not to make
    deigned not to make any
    not to make any reply
    to make any reply ,
    make any reply , but
    any reply , but ,
    reply , but , unable
    , but , unable to
    but , unable to contain
    , unable to contain herself
    unable to contain herself ,
    to contain herself , began
    contain herself , began scolding
    herself , began scolding one
    , began scolding one of
    began scolding one of her
    scolding one of her daughters
    one of her daughters .

Notice the ``-n`` argument to indicate the number of words that should be included in each ngram.

With all textkit commands, the ``--help`` flag shows all possible arguments for a command.


.. doctest::

    textkit words2ngrams --help

.. doctest::

  Usage: textkit words2ngrams [OPTIONS] [TOKENS]

      Tokenize words into ngrams. ngrams are n-length word tokens. Punctuation
      is considered as a separate token.

  Options:
    --sep TEXT            Separator between words in bigram output.  [default: ]
    -n, --length INTEGER  Length of the n-gram  [default: 2]
    --help                Show this message and exit.

Filter Tokens
-------------

textkit includes a number of filtering capabilities that can be useful for tweaking your tokens.

Notice our word and ngram tokens above include commas and periods? Let's remove them using ``filterpunc``.

.. doctest::

    textkit text2words input.txt | textkit filterpunc

If we don't want to pipe these commands together, we can also just execute filters on the ``words.txt`` - the saved word token file.

.. doctest::

    textkit filterpunc words.txt


In natural language processing, ``stop words`` are words so common that they provide little information about a document, and so are often removed. Textkit's ``filterwords`` will remove stop words from our token output.


.. doctest::

    textkit filterwords words.txt

We can also just filter words that are less then a certain number of characters long:

.. doctest::

    textkit filterlengths -m 5 words.txt

This would produce:

.. doctest::

    Bennet
    deigned
    reply
    unable
    contain
    herself
    began
    scolding
    daughters

Transform Tokens
----------------

There are a number of tools in textkit to transform tokens in varous ways.

Ensuring the casing of our tokens is consistent is a common text analysis preprocessing step.

This is done in textkit using ``tokens2lower`` and ``tokens2upper``. These commands work on tokens as well as raw text.

.. doctest::

    textkit tokens2lower input.txt

.. doctest::

    mrs. bennet deigned not to make any reply, but, unable to contain
    herself, began scolding one of her daughters.


.. doctest::

    textkit tokens2upper words.txt

.. doctest::

    MRS. BENNET DEIGNED NOT TO MAKE ANY REPLY, BUT, UNABLE TO CONTAIN
    HERSELF, BEGAN SCOLDING ONE OF HER DAUGHTERS.

Token Information and Stats
---------------------------

textkit is also great for finding out interesting stuff about your text.

Count unique tokens with ``tokens2counts``, which outputs a CSV-like output that includes the token and the count of that token in the document.

.. doctest::

    textkit tokens2counts words.txt

``TODO: topbigrams``

``TODO: tokens2pos``

Package
-------

Once the tokens are setup and transformed the way you want them,
it can be useful to package up a set of documents into a single file for downstream visualization or other uses.

.. doctest::

    textkit tokens2json words1.txt words2.txt > out.json
