from nltk.tokenize import sent_tokenize
import click
from textkit.utils import output

@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def text2sentences(text):
    '''Tokenize text into sentence tokens.'''
    content = '\n'.join([open(f).read() for f in text])
    sentences = sent_tokenize(content)
    [output(s.strip()) for s in sentences]
