import click
from string import punctuation
from textkit.utils import output, read_tokens


@click.command()
@click.argument('tokens', type=click.File('r'))
@click.option('-m', '--min', default=3,
              help='Minimum length of token to not filter.', show_default=True)
def filterlengths(min, tokens):
    '''Remove tokens that are shorter then the minimum length provided.'''
    content = read_tokens(tokens)
    [output(token) for token in content
        if len(token) >= min]
