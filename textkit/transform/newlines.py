import click
from textkit.utils import output


@click.command()
@click.argument('text', type=click.File('r'))
def nonewlines(text):
    '''Remove newlines from a text file.'''
    content = text.read()
    content = content.replace('\n', ' ').strip()
    output(content)
