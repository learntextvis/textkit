import click
from click.testing import CliRunner
from textkit.stats.count_tokens import count_tokens
from textkit.stats.top_bigrams import top_bigrams
from tests.utils import create_single_output, create_multifile_output, compare_results

def test_count_tokens():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nworld\n!\nI\nlove\nthis\nworld\nand\nlove\nyou'
        expected_tokens = ['love,2', 'world,2', 'and,1', 'I,1', 'you,1', 'this,1', 'Hello,1', '!,1', '']
        expected_tokens.sort()
        create_single_output(filename, sentence)
        result = runner.invoke(count_tokens, [filename])
        tokens = result.output.split('\n')
        tokens.sort()
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)

# Need to write test for top bigrams!