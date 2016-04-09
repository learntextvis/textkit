import os
import click
import nltk
from textkit.utils import output, read_tokens, data_item


@click.command('tokens2pos')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('--sep', default=' ',
              help='Separator between words in the output.',
              show_default=True)
def tokens2pos(sep, tokens):
    '''Tokenize words into their parts of speech. Each item
    is the original word with its role as the second part
    of the item. Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    nltk.data.path.append(data_item())
    tags = nltk.pos_tag(content)
    [output("{},{}".format(t[0], t[1])) for t in tags]
