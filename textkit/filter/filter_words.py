import os
import click
from textkit.utils import output, read_tokens, data_item

def get_stopwords(stopword_name):
    path = data_item('/stopwords/' + stopword_name + '.txt')
    stopwords = []
    with open(path) as filename:
        stopwords = read_tokens(filename)
    return stopwords


@click.command()
@click.option('-l', '--language', type=click.Choice(['english', 'german']),
              default='english')
@click.option('--custom', type=click.File('r'),
              help='Optional token file of additional tokens to remove ' +
              'along with selected stop words.')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
def filterwords(language, custom, tokens):
    '''Remove stop words from tokens, returning tokens without stop words.'''
    content = read_tokens(tokens)
    stopwords = get_stopwords(language)
    if custom:
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
