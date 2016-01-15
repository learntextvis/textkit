import click
import nltk
import re
from string import punctuation
from textkit.utils import output


@click.command()
@click.argument('text', type=click.File('r'))
def text2punc(text):
    '''Tokenize text into punctuation tokens.
    Words and numbers are removed, leaving only punctuation.'''

    # from: http://stackoverflow.com/questions/17485092/how-to-just-keep-punctuation-with-a-string-in-python

    content = text.read()
    out = re.sub(r'[^{}]+'.format(punctuation), ' ', content)
    out = out.split()
    [output(p) for p in out]
