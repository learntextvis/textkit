import click
import nltk
from textkit.utils import write_csv, read_tokens


@click.command('words2ngrams')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
@click.option('-n', '--num', default=2,
              help='Length of the n-gram',
              show_default=True)
def words2ngrams(sep, num, tokens):
    '''Convert word tokens into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    ngrams = list(nltk.ngrams(content, num))
    write_csv(ngrams, str(sep))


@click.command('text2ngrams')
@click.argument('text', type=click.Path(exists=True), nargs=-1)
@click.option('-s', '--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
@click.option('-n', '--num', default=2,
              help='Length of the n-gram',
              show_default=True)
def text2ngrams(sep, num, text):
    '''Tokenize plain text into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''
    content = '\n'.join([open(f).read() for f in text])
    tokens = nltk.word_tokenize(content)
    ngrams = list(nltk.ngrams(tokens, num))
    write_csv(ngrams, str(sep))
