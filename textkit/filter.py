import click
from string import punctuation


@click.command()
@click.option('--out', type=click.File('w'), default='-',
              help='Optional output file. Defaults to standard out.')
# @click.option('--punctuation', default=punctuation,
#               help='String indicating punctuation to check for.')
@click.argument('tokens', type=click.File('r'))
def filterpunc(out, tokens):
    '''Remove tokens that are only punctuation from a list of tokens'''
    content = tokens.read().split('\n')
    [click.echo(token, file=out) for token in content
        if token not in punctuation]
