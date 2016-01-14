import click
from textkit.tokenize.words import text2words
from textkit.tokenize.sentences import text2sentences
from textkit.filter.filter_punc import filterpunc
from textkit.stats.count_tokens import count_tokens
from textkit.transform.lowercase import lowercase
from textkit.transform.uppercase import uppercase
from textkit.package.to_json import tokens2json


@click.group()
def cli():
    '''Text analysis from the command line.
    '''
    pass

cli.add_command(text2words)
cli.add_command(text2sentences)
cli.add_command(filterpunc)
cli.add_command(count_tokens)
cli.add_command(lowercase)
cli.add_command(uppercase)
cli.add_command(tokens2json)
