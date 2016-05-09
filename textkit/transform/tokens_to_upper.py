import click
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
def tokens2upper(tokens):
    '''Transform all tokens to uppercase.'''
    content = read_tokens(tokens)
    [output(token.upper()) for token in content]
