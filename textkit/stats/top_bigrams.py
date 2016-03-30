import click
import nltk
from textkit.utils import read_tokens, output


MEASURES = dict({
    'likelihood': nltk.collocations.BigramAssocMeasures.likelihood_ratio,
    'chi_sq': nltk.collocations.BigramAssocMeasures.chi_sq,
    'pmi': nltk.collocations.BigramAssocMeasures.pmi,
    'student_t': nltk.collocations.BigramAssocMeasures.student_t,
    'freq': nltk.collocations.BigramAssocMeasures.raw_freq
})


@click.command('topbigrams')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('--sep', default=' ',
              help='Separator between tokens and scores in output.',
              show_default=True)
@click.option('-m', '--measure', type=click.Choice(list(MEASURES.keys())),
              default=list(MEASURES.keys())[0],
              help='Specify which measure to use to define interesing-ness.',
              show_default=True)
@click.option('--freq', default=2,
              help='Minimum frequency of bi-grams to filter out.',
              show_default=True)
@click.option('--scores/--no-scores', default=False,
              help='Include or exclude scores in output.',
              show_default=True)
def top_bigrams(sep, measure, freq, scores, tokens):
    '''Find top most interesting bi-grams in a token document.
    Uses the --measure argument to determine what measure to use to define
    'interesting'.
    '''

    output(sep)
    content = read_tokens(tokens)
    bcf = nltk.collocations.BigramCollocationFinder.from_words(content)
    bcf.apply_freq_filter(freq)

    nltk_measure = MEASURES[measure]
    bigrams = bcf.score_ngrams(nltk_measure)

    out = [b[0] for b in bigrams]
    if scores:
        out = [b[0] + tuple([str(b[1])]) for b in bigrams]
    [output(sep.join(line)) for line in out]
