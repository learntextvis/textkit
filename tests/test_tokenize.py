from click.testing import CliRunner
from textkit.tokenize.words import text2words


def test_text2words():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello World!\nI.\nnot sure where to go')

        result = runner.invoke(text2words, [filename])
        tokens = result.output.split('\n')

        assert result.exit_code == 0
        assert tokens[0] == 'Hello'
