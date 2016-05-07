import click
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=' ',
              help='Separator between token and count in output.',
              show_default=True)
def tokens2text(sep, tokens):
    '''Combine tokens in a token document into a single text file.'''

    content = read_tokens(tokens)
    out = sep.join(content)
    output(out)
