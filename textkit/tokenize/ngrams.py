import click
import nltk
from textkit.utils import output, read_tokens


@click.command()
@click.argument('tokens', type=click.File('r'))
@click.option('--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
@click.option('-n', '--n', default=2,
              help='Length of the n-gram',
              show_default=True)

def words2ngrams(sep, n, tokens):
    '''Tokenize words into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    ngrams = list(nltk.ngrams(content, n))
    [output(sep.join(ngram)) for ngram in ngrams]
