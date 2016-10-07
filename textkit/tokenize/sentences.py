from nltk.tokenize import sent_tokenize
import click
from textkit.utils import output

@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def text2sentences(text):
    '''Tokenize text into sentence tokens.'''
    content = '\n'.join([open(f).read() for f in text])
    sentences = []
    try:
        sentences = sent_tokenize(content)
    except LookupError as err:
        click.echo(message="Error with tokenization", nl=True)
        click.echo(message="Have you run \"textkit download\"?", nl=True)
        click.echo(message="\nOriginal Error:", nl=True)
        click.echo(err)
    [output(s.strip()) for s in sentences]
