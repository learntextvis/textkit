import click
import nltk
from textkit.utils import output


@click.command()
@click.argument('text', type=click.Path(exists=True), nargs=-1)
def text2words(text):
    '''Tokenize text into word tokens.
    Punctuation is considered as a separate token.'''
    content = '\n'.join([open(f).read() for f in text])
    tokens = []
    try:
        tokens = nltk.word_tokenize(content)
    except LookupError as err:
        click.echo(message="Error with tokenization", nl=True)
        click.echo(message="Have you run \"textkit download\"?", nl=True)
        click.echo(message="\nOriginal Error:", nl=True)
        click.echo(err)
    [output(token) for token in tokens]
