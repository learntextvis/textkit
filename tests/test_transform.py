
from click.testing import CliRunner
from textkit.transform.lowercase import lowercase


def test_lowercase():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\n.\nnoooo\n')

        result = runner.invoke(lowercase, [filename])

        assert result.exit_code == 0
        assert result.output.split('\n')[0] == 'hello'
        assert result.output.split('\n')[1] == 'world'
