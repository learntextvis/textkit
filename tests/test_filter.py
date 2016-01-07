import click
from click.testing import CliRunner
from textkit.filter import filterpunc


def test_filterpunc():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('in.txt', 'w') as f:
            f.write('Hello\nWorld\n!\nI\n.\nnot')

        result = runner.invoke(filterpunc, ['in.txt'])
        assert result.exit_code == 0
        assert '!' not in result.output
        assert '.' not in result.output
