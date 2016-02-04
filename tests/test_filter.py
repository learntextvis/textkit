import click
from click.testing import CliRunner
from textkit.filter.filter_punc import filterpunc
from textkit.filter.filter_words import filterwords


def test_filterpunc():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\n.\nnot')

        result = runner.invoke(filterpunc, [filename])

        assert result.exit_code == 0
        assert '!' not in result.output
        assert '.' not in result.output


def test_filterwords():
    runner = CliRunner()
    with runner.isolated_filesystem():

        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\nam\nnot\na\ncrook\n.')

        result = runner.invoke(filterwords, ['--language', 'english', filename])

        assert result.exit_code == 0
        assert 'I' not in result.output
        assert 'am' not in result.output

def test_filterwords_custom():
    runner = CliRunner()
    with runner.isolated_filesystem():

        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\nam\nnot\na\ncrook\n.')

        filename = 'custom.txt'
        with open(filename, 'w') as f:
            f.write('hello\n')

        result = runner.invoke(filterwords, ['--custom', 'custom.txt', filename])

        assert result.exit_code == 0
        assert 'I' not in result.output
        assert 'am' not in result.output
        assert 'Hello' not in result.output
