import click
import os
from string import punctuation
from textkit.utils import output, read_tokens


def get_stopwords(id):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    path = cur_dir + "/../../data/stopwords/" + id + ".txt"
    stopwords = []
    with open(path) as f:
        stopwords = read_tokens(f)
    return stopwords


@click.command()
@click.option('-l', '--language', type=click.Choice(['english', 'german']),
              default='english')
@click.option('--custom', type=click.File('r'),
              help='Optional token file of additional tokens to remove along with selected stop words.')
@click.argument('tokens', type=click.File('r'))
def filterwords(language, custom, tokens):
    '''Remove stop words from tokens, returning tokens without stop words.'''
    content = read_tokens(tokens)
    stopwords = get_stopwords(language)
    if(custom):
        stopwords = stopwords + read_tokens(custom)

    [output(token) for token in content
        if token.lower() not in stopwords]


@click.command()
@click.option('-l', '--language', type=click.Choice(['english', 'german']),
              default='english')
def showstops(language):
    '''Display stop words used by textkit for a given language.'''
    stopwords = get_stopwords(language)

    [output(token) for token in stopwords]
