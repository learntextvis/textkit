import click
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import EnglishStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from textkit.utils import read_tokens, output


@click.command()
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('--algorithm', default='porter',
              help='Choice of stemming algorithm: porter, lancaster, snowball, wordnet',
              type=click.STRING,
              show_default=True)
def stem(tokens, algorithm):
    '''Apply stemming to an iterable of tokens.'''
    content = read_tokens(tokens)

    stemmer_classes = {'porter': PorterStemmer,
                       'lancaster': LancasterStemmer,
                       'snowball': EnglishStemmer}
    if algorithm.lower() == 'wordnet':
        stemmer = WordNetLemmatizer()
        for token in content:
            output(stemmer.lemmatize(token))

    elif algorithm.lower() in stemmer_classes:
        stemmer = stemmer_classes[algorithm.lower()]()
        for token in content:
            output(stemmer.stem(token))

    else:
        # passthrough if algorithm is invalid
        for token in content:
            output(token)
