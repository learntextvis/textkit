import re
import click
from textkit.utils import output


@click.command()
@click.argument('text', type=click.File('r'))
def text2sentences(text):
    '''Tokenize text into sentence tokens.'''
    content = text.read()
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    [output(s.strip()) for s in sentences]
