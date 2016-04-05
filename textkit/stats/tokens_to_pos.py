import os
import click
import nltk
from textkit.utils import output, read_tokens, data_dir

@click.command('words2pos')
@click.argument('tokens', type=click.File('r'))
@click.option('--sep', default=' ',
              help='Separator between words in the output.',
              show_default=True)

def tokens2pos(sep, tokens):
    '''Tokenize words into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    nltk.data.path.append(data_dir())
    tags = nltk.pos_tag(content)
    [output("{},{}".format(t[0], t[1])) for t in tags]
