import click
import nltk
from textkit.utils import output, read_tokens


@click.command('words2ngrams')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
@click.option('-n', '--length', default=2,
              help='Length of the n-gram',
              show_default=True)
def words2ngrams(sep, length, tokens):
    '''Tokenize words into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    ngrams = list(nltk.ngrams(content, length))
    [output(sep.join(ngram)) for ngram in ngrams]
