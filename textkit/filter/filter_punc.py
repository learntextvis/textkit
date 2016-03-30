from string import punctuation
import click
from textkit.utils import output, read_tokens


@click.command()
# @click.option('--out', type=click.File('w'), default='-',
#               help='Optional output file. Defaults to standard out.')
# @click.option('--punctuation', default=punctuation,
#               help='String indicating punctuation to check for.')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
def filterpunc(tokens):
    '''Remove tokens that are only punctuation from a list of tokens.'''
    content = read_tokens(tokens)
    [output(token) for token in content if token not in punctuation]
