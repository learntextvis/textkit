import re
import click


@click.command()
@click.argument('text', type=click.File('r'))
def text2sentences(text):
    '''Tokenize text into sentence tokens'''
    content = text.read()
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', content)
    [click.echo(s.strip()) for s in sentences]
