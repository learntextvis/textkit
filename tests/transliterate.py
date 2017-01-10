import click
from click.testing import CliRunner
from textkit.filter.transliterate import transliterate


def test_transliterate():
    runner = CliRunner()
    filename = 'test_data/international.txt'
    ## ???
