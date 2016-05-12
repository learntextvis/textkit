# encoding=utf8
import click
import math
import nltk
from collections import defaultdict
from textkit.utils import read_tokens, write_csv


# input document_tokens: a list of tokens that represent a document
# input corpus_tokens: list of lists of tokens.
#  One list for each document in the corpora.
# output: list of (token, tf-idf) values
#         for each unique token in document_tokens
@click.command('tokens2tfidf')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.argument('corpus',  type=click.Path(exists=True), nargs=-1)
@click.option('-s', '--sep', default=' ',
              help='Separator between token and tf-idf scroe in output.',
              show_default=True)
# @click.option('-c', '--corpus', type=click.Path(exists=True),
#               help='Set of corpus tokens to compare document to.')
def tokens2tfidf(sep, tokens, corpus):
    '''
    Compute TF-IDF for a set of tokens given a folder or set of files
    representing a corpus to compare the tokens to.
    '''
    content = read_tokens(tokens)
    corpus_all = [open(f).read() for f in corpus]
    # if six.PY2:
    #     corpus_all = [d.decode('utf-8') for d in corpus_all]
    corpus_tokens = [nltk.word_tokenize(d) for d in corpus_all]

    # corpus_tokens = [read_tokens(open(f, 'r')) for f in corpus]

    # Get our token frequencies for all the unique tokens in our document
    token_counts = get_counts(content)

    # iterate through these tokens and calculate the tf-idf
    tfidfs = {}
    for token in token_counts.keys():

        tf = term_frequency(token, token_counts)
        idf = inverse_doc_frequency(token, corpus_tokens)

        tfidfs[token] = tf * idf

    scores = sort_scores(tfidfs)
    rows = [list(map(str, vals)) for ind, vals in enumerate(scores)]
    write_csv(rows, str(sep))


def sort_scores(scores):
    '''Sorts dict of scores by score and returns array of scores'''
    return sorted(scores.items(), key=lambda count: count[1], reverse=True)


def get_counts(tokens):
    '''Count unique tokens in a list'''
    counts = defaultdict(int)
    for token in tokens:
        counts[token] += 1
    return counts


# input token: the token we are looking at
# input counts: token count dictionary for one document
def term_frequency(token, counts):
    '''Calculate term frequency for a
       particular token in a particular document'''
    return counts[token] / float(len(counts.keys()))


# input: token: token we are analyzing
# input: corpus_tokens: list of lists of tokens.
#  One list for each document in the corpora.
def inverse_doc_frequency(token, corpus_tokens):
    return math.log(1 + len(corpus_tokens) /
                    (document_frequency(token, corpus_tokens) + 1))


# input token: a token to search the corpora for
# input corpus_tokens: list of lists of tokens.
#  One list for each document in the corpora.
# output: number of documents in corpora that contain the token.
def document_frequency(token, corpus_tokens):
    '''Returns number of times a token appears in a set of documents'''
    doc_count = 0
    for tokens in corpus_tokens:

        if token in tokens:
            doc_count += 1

    return doc_count
