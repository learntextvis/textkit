import click
import nltk
from textkit.utils import output


@click.command()
@click.argument('text', type=click.File('r'))
def text2words(text):
    '''Tokenize text into word tokens.
    Punctuation is considered as a separate token.'''

    content = text.read()
    tokens = nltk.word_tokenize(content)
    [output(token) for token in tokens]
