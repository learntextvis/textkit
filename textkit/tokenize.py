import re
import click


@click.command()
@click.argument('text', type=click.File('r'))
def text2words(text):
    '''Tokenize text into word tokens'''
    content = text.read()
    [click.echo(w) for w in content.split()]


@click.command()
@click.argument('text', type=click.File('r'))
def text2sentences(text):
    '''Tokenize text into sentence tokens'''
    content = text.read()
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    [click.echo(s.strip()) for s in sentences]
