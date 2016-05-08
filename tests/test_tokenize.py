from click.testing import CliRunner
from textkit.tokenize.words import text2words
from textkit.tokenize.bigrams import words2bigrams
from textkit.tokenize.punc import text2punc
from textkit.tokenize.sentences import text2sentences
from textkit.tokenize.ngrams import words2ngrams
from tests.utils import create_single_output, create_multifile_output, compare_results


def test_text2words():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello World!\nI.\nnot sure where to go'
        expected_tokens = ['Hello', 'World', '!', 'I.',
                           'not', 'sure', 'where', 'to', 'go']
        create_single_output(filename, sentence)
        result = runner.invoke(text2words, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_text2words_multifile():
    runner = CliRunner()
    with runner.isolated_filesystem():

        filenames = ['in.txt', 'in2.txt']
        sentences = ('Hello World!\nI.\nnot sure where to go',
                     'Goodbye World!\n I.\n know everything about you')
        expected_tokens = ['Hello', 'World', '!', 'I.',
                           'not', 'sure', 'where', 'to', 'go',
                           'Goodbye', 'World', '!', 'I.', 'know',
                           'everything', 'about', 'you']
        create_multifile_output(filenames, sentences)
        result = runner.invoke(text2words, filenames)
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_words2bigrams():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nlove\ngo\n.'
        expected_tokens = ['Hello World', 'World !',
                           '! I', 'I love', 'love go', 'go .']
        create_single_output(filename, sentence)
        result = runner.invoke(words2bigrams, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_sentences():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello World! I love go.'
        expected_tokens = ['Hello World!', 'I love go.']
        create_single_output(filename, sentence)
        result = runner.invoke(text2sentences, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_punc():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nlove,\ngo\n.'
        expected_tokens = ['!', ',', '.']
        create_single_output(filename, sentence)
        result = runner.invoke(text2punc, [filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_punc_multifile():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filenames = ['in.txt', 'in2.txt']
        sentences = ['Hello\nWorld\n!\nI\nlove,\ngo\n.',
                     'Goodbye World!\n I...\n know everything\'s about you?']
        expected_tokens = ['!', ',', '.', '!', '...', "'", '?']
        create_multifile_output(filenames, sentences)
        result = runner.invoke(text2punc, filenames)
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)


def test_words2ngrams():
    runner = CliRunner()
    with runner.isolated_filesystem():
        filename = 'in.txt'
        sentence = 'Hello\nWorld\n!\nI\nlove\ngo\n.'
        expected_tokens = ['Hello World !', 'World ! I', '! I love', 'I love go']
        create_single_output(filename, sentence)
        result = runner.invoke(words2ngrams, ['-n', 3, filename])
        tokens = result.output.split('\n')
        assert result.exit_code == 0
        compare_results(tokens, expected_tokens)
