import click

@click.group()
def cli():
    pass

@click.command()
def text2words():
    click.echo('convert text to word tokens')

@click.command()
def text2sentences():
    click.echo('convert text to sentence tokens')

cli.add_command(text2words)
cli.add_command(text2sentences)
