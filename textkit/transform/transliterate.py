import click
from textkit.utils import read_tokens, output
from unidecode import unidecode
import chardet

@click.command()
@click.argument('file', type=click.File('r'), default=click.open_file('-'))
def transliterate(file):
    '''Transliterate international text to ascii.'''
    content = ''.join(file.readlines())
    content = content.decode(chardet.detect(content)['encoding'])
    [output(unidecode(content).encode('ascii','ignore'))]
