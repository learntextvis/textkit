import click
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'))
def lowercase(tokens):
    '''Transform all tokens to lowercase.'''
    content = read_tokens(tokens)
    [output(token.lower()) for token in content]
