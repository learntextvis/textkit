import click
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'))
def uppercase(tokens):
    '''Transform all tokens to uppercase.'''
    content = read_tokens(tokens)
    [output(token.upper()) for token in content]
