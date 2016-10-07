import click
import nltk
from textkit.utils import output, read_tokens


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
def words2bigrams(sep, tokens):
    '''Tokenize words into bigrams. Bigrams are two word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    bigrams = []
    try:
        bigrams = list(nltk.bigrams(content))
    except LookupError as err:
        click.echo(message="Error with tokenization", nl=True)
        click.echo(message="Have you run \"textkit download\"?", nl=True)
        click.echo(message="\nOriginal Error:", nl=True)
        click.echo(err)
    [output(sep.join(bigram)) for bigram in bigrams]
