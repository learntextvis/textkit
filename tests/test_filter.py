import click
from click.testing import CliRunner
from textkit.filter.filter_punc import filterpunc


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
