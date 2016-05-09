import click
import nltk
from collections import OrderedDict
from textkit.utils import read_tokens, write_csv


MEASURES = OrderedDict([
    ('likelihood', nltk.collocations.BigramAssocMeasures.likelihood_ratio),
    ('chi_sq', nltk.collocations.BigramAssocMeasures.chi_sq),
    ('pmi', nltk.collocations.BigramAssocMeasures.pmi),
    ('student_t', nltk.collocations.BigramAssocMeasures.student_t),
    ('freq', nltk.collocations.BigramAssocMeasures.raw_freq)
])


@click.command('tokens2topbigrams')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=',',
              help='Separator between tokens and scores in output.',
              show_default=True)
@click.option('-m', '--measure', type=click.Choice(list(MEASURES.keys())),
              default=list(MEASURES.keys())[0],
              help='Specify which measure to use to define interesing-ness.',
              show_default=True)
@click.option('--freq', default=2,
              help='Minimum frequency of bi-grams to filter out.',
              show_default=True)
@click.option('--scores/--no-scores', default=True,
              help='Include or exclude scores in output.',
              show_default=True)
def tokens2topbigrams(sep, measure, freq, scores, tokens):
    '''Find top most interesting bi-grams in a token document.
    Uses the --measure argument to determine what measure to use to define
    'interesting'.
    '''

    content = read_tokens(tokens)
    bcf = nltk.collocations.BigramCollocationFinder.from_words(content)
    bcf.apply_freq_filter(freq)

    nltk_measure = MEASURES[measure]
    bigrams = bcf.score_ngrams(nltk_measure)

    out = [b[0] for b in bigrams]
    if scores:
        out = [b[0] + tuple([str(b[1])]) for b in bigrams]
    write_csv(out, str(sep))
