import os
import click
import nltk
from textkit.utils import write_csv, read_tokens, data_item


@click.command('tokens2pos')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=',',
              help='Separator between words in the output.',
              show_default=True)
def tokens2pos(sep, tokens):
    '''Tokenize words into their parts of speech. Output contains the
       word token followed by its part-of-speech tag, separated by the
       character specified by --sep.
    '''

    content = read_tokens(tokens)
    nltk.data.path.append(data_item())
    tags = nltk.pos_tag(content)
    write_csv(tags, str(sep))
