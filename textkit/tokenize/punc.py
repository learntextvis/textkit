import re
from string import punctuation
import click
from textkit.utils import output

@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def text2punc(text):
    '''Tokenize text into punctuation tokens.
    Words and numbers are removed, leaving only punctuation.'''

    # from: http://stackoverflow.com/questions/17485092/how-to-just-keep-punctuation-with-a-string-in-python

    content = '\n'.join([open(f).read() for f in text])
    out = re.sub(r'[^{}]+'.format(punctuation), ' ', content)
    out = out.split()
    [output(p) for p in out]
