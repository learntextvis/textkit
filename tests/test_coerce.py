
from textkit.coerce import coerce_types


def test_coerce_types():
    content = [
        ["happy", "9"],
        ["day", "8"],
        ["4", "7"],
        ["YOU!", "6"]
    ]

    tokens = coerce_types(content)
    assert len(tokens) == 4
    assert tokens[0][0] == "happy"
    assert tokens[0][1] == 9
    assert tokens[2][0] == "4"


def test_coerce_types_with_mix_floats_ints():
    content = [
        ["happy", "9"],
        ["day", "8.7"],
        ["4", "7.0"],
        ["YOU!", "6"]
    ]

    tokens = coerce_types(content)
    assert len(tokens) == 4
    assert tokens[0][0] == "happy"
    assert tokens[0][1] == 9.0
    assert tokens[1][1] == 8.7
    assert tokens[2][1] == 7
