import click
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
def tokens2lower(tokens):
    '''Transform all tokens to lowercase.'''
    content = read_tokens(tokens)
    [output(token.lower()) for token in content]
