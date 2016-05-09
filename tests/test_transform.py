
from click.testing import CliRunner
from textkit.transform.tokens_to_lower import tokens2lower
from textkit.transform.newlines import nonewlines
from textkit.transform.tokens_to_upper import tokens2upper
from textkit.transform.tokens_to_counts import tokens2counts
from textkit.transform.tokens_to_pos import tokens2pos
from textkit.transform.tokens_to_top_bigrams import tokens2topbigrams
from tests.utils import create_single_output, create_multifile_output, compare_results


def test_lowercase():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\n.\nnoooo\n'
        expected_tokens = ['hello', 'world', '!', 'i', '.', 'noooo']
        create_single_output(filename, sentence)

        result = runner.invoke(tokens2lower, [filename])
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

        result = runner.invoke(tokens2upper, [filename])
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


def test_count_tokens():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello,\nworld\n!\nI\nlove\nthis\nworld\nand\nlove\nyou'
        expected_tokens = ['love,2', 'world,2', 'and,1', 'I,1', 'you,1',
                           'this,1', '\"Hello,\",1', '!,1', '']
        expected_tokens.sort()
        create_single_output(filename, sentence)
        result = runner.invoke(tokens2counts, [filename])
        tokens = result.output.split('\n')
        tokens.sort()
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_pos_tokens():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nworld\n!\nI\nlove\nthis\nworld\nand\nlove\nyou'
        expected_tokens = ['Hello,NNP', 'world,NN', '!,.',
                           'I,PRP', 'love,VBP', 'this,DT',
                           'world,NN', 'and,CC', 'love,VB', 'you,PRP']
        create_single_output(filename, sentence)
        result = runner.invoke(tokens2pos, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_top_bigrams():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'I\nworld\n!\nI\nlove\nyou\nthis\nworld\nand\nlove\nyou'
        create_single_output(filename, sentence)

        result = runner.invoke(tokens2topbigrams, [filename])
        assert result.exit_code == 0

        tokens = result.output.split('\n')
        assert tokens[0].split(',')[0:2] == ['love', 'you']
