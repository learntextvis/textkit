
from click.testing import CliRunner
from textkit.transform.lowercase import lowercase
from textkit.transform.newlines import nonewlines
from textkit.transform.uppercase import uppercase
from tests.utils import create_single_output, create_multifile_output, compare_results


def test_lowercase():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\n.\nnoooo\n'
        expected_tokens = ['hello', 'world', '!', 'i', '.', 'noooo']
        create_single_output(filename, sentence)

        result = runner.invoke(lowercase, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_uppercase():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\n.\nnoooo\n'
        expected_tokens = ['HELLO', 'WORLD', '!', 'I', '.', 'NOOOO']
        create_single_output(filename, sentence)

        result = runner.invoke(uppercase, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_nonewlines():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nam\nin.\n'
        expected_tokens = ['Hello World ! I am in.']

        create_single_output(filename, sentence)
        result = runner.invoke(nonewlines, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        assert len(result.output.split('\n')) == 2
        compare_results(tokens, expected_tokens)


def test_nonewlines_multifile():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filenames = ['in.txt', 'in2.txt']
        sentences = ['Hello\nWorld\n!\nI\nam\nin.',
                     'What are you\na creature\nof mystery']
        expected_tokens = ['Hello World ! I am in. What are you a creature of mystery']
        create_multifile_output(filenames, sentences)
        result = runner.invoke(nonewlines, filenames)
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        assert len(result.output.split('\n')) == 2
        compare_results(tokens, expected_tokens)
