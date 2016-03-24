from click.testing import CliRunner
from textkit.tokenize.words import text2words
from textkit.tokenize.bigrams import words2bigrams
from textkit.tokenize.ngrams import words2ngrams


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


def test_words2bigrams():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\nlove\ngo\n.')

        result = runner.invoke(words2bigrams, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        assert tokens[0] == 'Hello World'
        assert tokens[1] == 'World !'

def test_words2ngrams():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        with open(filename, 'w') as f:
            f.write('Hello\nWorld\n!\nI\nlove\ngo\n.')

        result = runner.invoke(words2ngrams, ['-n', 3, filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        assert tokens[0] == 'Hello World !'
        assert tokens[1] == 'World ! I'
        assert tokens[2] == '! I love'