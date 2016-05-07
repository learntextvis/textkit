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
    bigrams = list(nltk.bigrams(content))
    [output(sep.join(bigram)) for bigram in bigrams]
