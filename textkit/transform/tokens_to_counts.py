import click
from collections import defaultdict
from textkit.utils import read_tokens, write_csv


@click.command('tokens2counts')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=',',
              help='Separator between token and count in output.',
              show_default=True)
@click.option('--limit', default=-1, type=click.INT,
              help='Only output the top N most frequent tokens')
def tokens2counts(sep, limit, tokens):
    '''Count unique tokens in a list of tokens.
    Tokens are sorted by top counts.'''
    content = read_tokens(tokens)
    counts = sort_counts(get_counts(content))

    # we want the argument type to be an INT - but python only
    # has support for a float infinity. So if it the limit is negative,
    # it becomes infinite
    if limit < 0:
        limit = float('inf')

    # using csv writer to ensure proper encoding of the seperator.
    rows = [list(map(str, vals)) for ind, vals in enumerate(counts) if ind < limit]
    write_csv(rows, str(sep))


def get_counts(tokens):
    '''Count unique tokens in a list'''
    counts = defaultdict(int)
    for token in tokens:
        counts[token] += 1
    return counts


def sort_counts(counts):
    '''Sorts dict of counts by count and returns array of counts'''
    return sorted(counts.items(), key=lambda count: count[1], reverse=True)
