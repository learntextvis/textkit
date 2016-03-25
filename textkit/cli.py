#!/usr/bin/env python

import click
from textkit.tokenize.words import text2words
from textkit.tokenize.sentences import text2sentences
from textkit.tokenize.bigrams import words2bigrams
from textkit.tokenize.ngrams import words2ngrams
from textkit.tokenize.punc import text2punc
from textkit.filter.filter_punc import filterpunc
from textkit.filter.filter_words import filterwords
from textkit.filter.filter_lengths import filterlengths
from textkit.filter.filter_words import showstops
from textkit.transform.lowercase import lowercase
from textkit.transform.uppercase import uppercase
from textkit.transform.newlines import nonewlines
from textkit.package.tokens_to_json import tokens2json
from textkit.package.texts_to_json import texts2json
from textkit.package.tokens_to_text import tokens2text
from textkit.stats.count_tokens import count_tokens
from textkit.stats.top_bigrams import top_bigrams

@click.group()
def cli():
    '''Text analysis from the command line.
    '''
    pass

cli.add_command(text2words)
cli.add_command(text2sentences)
cli.add_command(words2bigrams)
cli.add_command(words2ngrams)
cli.add_command(text2punc)
cli.add_command(filterpunc)
cli.add_command(filterwords)
cli.add_command(filterlengths)
cli.add_command(showstops)
cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(nonewlines)
cli.add_command(tokens2json)
cli.add_command(texts2json)
cli.add_command(tokens2text)
cli.add_command(count_tokens)
cli.add_command(top_bigrams)
