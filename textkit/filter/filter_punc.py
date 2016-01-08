import click
from string import punctuation
from textkit.utils import read_tokens


@click.command()
# @click.option('--out', type=click.File('w'), default='-',
#               help='Optional output file. Defaults to standard out.')
# @click.option('--punctuation', default=punctuation,
#               help='String indicating punctuation to check for.')
@click.argument('tokens', type=click.File('r'))
def filterpunc(tokens):
    '''Remove tokens that are only punctuation from a list of tokens.'''
    content = read_tokens(tokens)
    [click.echo(token) for token in content
        if token not in punctuation]
