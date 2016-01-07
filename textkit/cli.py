import click
from textkit.tokenize import text2words, text2sentences
from textkit.filter import filterpunc


# class Config(object):
#     def __init__(self):
#         self.verbose = False
#
# pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
def cli():
    pass

cli.add_command(text2words)
cli.add_command(text2sentences)
cli.add_command(filterpunc)
