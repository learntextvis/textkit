import click
from textkit.utils import output
from unidecode import unidecode
import chardet

@click.command()
@click.argument('file', type=click.File('r'), default=click.open_file('-'))
def transliterate(file):
    '''Convert international text to ascii.'''
    content = ''.join(file.readlines())
    try:
        content = content.decode(chardet.detect(content)['encoding'])
    except AttributeError:
        # Strings do not have a decode method in python 3.
        pass
    [output(unidecode(content).encode('ascii', 'ignore'))]
