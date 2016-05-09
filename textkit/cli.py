#!/usr/bin/env python

import click
from textkit.tokenize.words import text2words
from textkit.tokenize.sentences import text2sentences
from textkit.tokenize.bigrams import words2bigrams
from textkit.tokenize.ngrams import words2ngrams, text2ngrams
from textkit.tokenize.punc import text2punc
from textkit.filter.filter_punc import filterpunc
from textkit.filter.filter_words import filterwords
from textkit.filter.filter_lengths import filterlengths
from textkit.filter.filter_words import showstops
from textkit.transform.tokens_to_lower import tokens2lower
from textkit.transform.tokens_to_upper import tokens2upper
from textkit.transform.newlines import nonewlines
from textkit.transform.tokens_to_stem import tokens2stem
from textkit.transform.tokens_to_counts import tokens2counts
from textkit.transform.tokens_to_top_bigrams import tokens2topbigrams
from textkit.transform.tokens_to_pos import tokens2pos
from textkit.package.tokens_to_json import tokens2json
from textkit.package.texts_to_json import texts2json
from textkit.package.tokens_to_text import tokens2text
from textkit.download import download


@click.group()
def cli():
    '''Text analysis from the command line.
    '''
    pass

cli.add_command(text2words)
cli.add_command(text2sentences)
cli.add_command(words2bigrams)
cli.add_command(words2ngrams)
cli.add_command(text2ngrams)
cli.add_command(text2punc)
cli.add_command(filterpunc)
cli.add_command(filterwords)
cli.add_command(filterlengths)
cli.add_command(showstops)
cli.add_command(tokens2lower)
cli.add_command(tokens2upper)
cli.add_command(nonewlines)
cli.add_command(tokens2stem)
cli.add_command(tokens2json)
cli.add_command(texts2json)
cli.add_command(tokens2text)
cli.add_command(tokens2counts)
cli.add_command(tokens2topbigrams)
cli.add_command(tokens2pos)
cli.add_command(download)
