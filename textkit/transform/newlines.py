import click
import re
from textkit.utils import output


@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def nonewlines(text):
    '''Remove newlines from a text file.'''
    content = '\n'.join([open(f).read() for f in text])
    content = re.sub('\n|\r\n|\r', ' ', content).strip()
    output(content)
