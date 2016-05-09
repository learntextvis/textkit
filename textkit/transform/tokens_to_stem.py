import click
from collections import OrderedDict
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import EnglishStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from textkit.utils import read_tokens, output

ALGOS = OrderedDict([
    ('porter', PorterStemmer),
    ('lancaster', LancasterStemmer),
    ('snowball', EnglishStemmer),
    ('wordnet', WordNetLemmatizer)
])


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-a', '--algorithm', type=click.Choice(list(ALGOS.keys())),
              default=list(ALGOS.keys())[0],
              help='Specify which stemming algorithm to use.',
              show_default=True)
def tokens2stem(tokens, algorithm):
    '''Stem a list of tokens to get their root.'''
    content = read_tokens(tokens)
    stemmer = ALGOS[algorithm]()

    if algorithm == 'wordnet':
        for token in content:
            output(stemmer.lemmatize(token))
    else:
        for token in content:
            output(stemmer.stem(token))
