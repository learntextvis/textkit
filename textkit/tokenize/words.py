import re
import click


@click.command()
@click.argument('text', type=click.File('r'))
def text2words(text):
    '''Tokenize text into word tokens'''
    content = text.read()
    [click.echo(w) for w in content.split()]
