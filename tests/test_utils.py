
from textkit.utils import read_tokens


def test_read_tokens():
    f = open('test_data/word_tokens.txt', 'r')

    tokens = read_tokens(f)
    assert len(tokens) == 6

    f.close()
