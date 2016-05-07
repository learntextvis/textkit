import click
from click.testing import CliRunner
from textkit.stats.tokens_to_counts import tokens2counts
from textkit.stats.tokens_to_pos import tokens2pos
from textkit.stats.top_bigrams import top_bigrams
from tests.utils import create_single_output, create_multifile_output, compare_results


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

        result = runner.invoke(top_bigrams, [filename])
        assert result.exit_code == 0

        tokens = result.output.split('\n')
        assert tokens[0].split(',')[0:2] == ['love', 'you']
