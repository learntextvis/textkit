import click
import nltk
from textkit.utils import output


@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def text2words(text):
    '''Tokenize text into word tokens.
    Punctuation is considered as a separate token.'''
    content = '\n'.join([open(f).read() for f in text])
    tokens = nltk.word_tokenize(content)
    [output(token) for token in tokens]
