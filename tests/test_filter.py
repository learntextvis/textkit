import click
from click.testing import CliRunner
from textkit.filter.filter_punc import filterpunc
from textkit.filter.filter_words import filterwords
from textkit.filter.filter_lengths import filterlengths
from tests.utils import create_single_output, create_multifile_output, compare_results

def test_filterlengths():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\n.\nnot\nwin\n'
        
        create_single_output(filename, sentence)
        
        # default length 3
        result = runner.invoke(filterlengths, [filename])
        tokens = result.output.split('\n')
        expected_tokens = ['Hello', 'World', 'not', 'win'] 
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)

        # minumum length 4
        result = runner.invoke(filterlengths, ['-m', '4', filename])
        tokens = result.output.split('\n')
        expected_tokens = ['Hello', 'World']
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_filterpunc():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\n.\nnot'
        expected_tokens = ['Hello', 'World', 'I', 'not']
        create_single_output(filename, sentence)
        result = runner.invoke(filterpunc, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_filterwords():
    runner = CliRunner()
    with runner.isolated_filesystem():

        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nam\nnot\na\ncrook\n.'
        expected_tokens = ['Hello','World','!', 'crook','.']
        create_single_output(filename, sentence)
        result = runner.invoke(filterwords, ['--language', 'english', filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_filterwords_custom():
    runner = CliRunner()
    with runner.isolated_filesystem():

        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nam\nnot\na\ncrook\n.'
        expected_tokens = ['World','!','crook','.']
        custom_stopword_filename = 'custom.txt'
        custom_stopwords = 'hello\n'

        create_single_output(filename, sentence)
        create_single_output(custom_stopword_filename, custom_stopwords)

        result = runner.invoke(filterwords, ['--custom', 'custom.txt', filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)
