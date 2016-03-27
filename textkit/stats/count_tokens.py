import click
from textkit.utils import read_tokens, write_csv


@click.command('count')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('--sep', default=',',
              help='Separator between token and count in output.',
              show_default=True)
def count_tokens(sep, tokens):
    '''Count unique tokens in a list of tokens.
    Tokens are sorted by top counts.'''
    content = read_tokens(tokens)
    counts = sort_counts(get_counts(content))

    # using csv writer to ensure proper encoding of the seperator.
    rows = [map(str, vals) for vals in counts]
    write_csv(rows, sep)


def get_counts(tokens):
    '''Count unique tokens in a list'''
    counts = {}
    for token in tokens:
        if token in counts:
            counts[token] += 1
        else:
            counts[token] = 1
    return counts


def sort_counts(counts):
    '''Sorts dict of counts by count and returns array of counts'''
    return sorted(counts.items(), key=lambda count: count[1], reverse=True)
