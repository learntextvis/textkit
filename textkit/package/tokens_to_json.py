import sys
import json
from collections import OrderedDict
import click
from textkit.utils import output, read_tokens, read_csv
from textkit.coerce import coerce_types


def read_names(names_path):
    names = []
    if names_path:
        names_doc = open(names_path, 'r')
        names = read_tokens(names_doc)
    return names


@click.command()
@click.argument('token_docs', type=click.Path(exists=True), nargs=-1)
@click.option('--ids', type=click.Path(),
              help="File with one id per token document, each separated " +
              "by a new line. Ids file is used to set the id attribute in " +
              "the output JSON.")
@click.option('--names', type=click.Path(),
              help="File with one name per token document, each separated " +
              "by a new line. Names file is used to set the name attribute " +
              "in the output JSON.")
@click.option('--field', default='tokens', help="Attribute name where " +
              "tokens will be stored in the document object.",
              show_default=True)
@click.option('--split/--no-split', default=False, help="If enabled, " +
              "textkit will attempt to split input columns when " +
              "packaging. This is useful when packaging multiple column " +
              "output like counts.",
              show_default=True)
@click.option('-s', '--sep', default=',', help="Separator character between " +
              "columns. Only used if split-columns flag is used.",
              show_default=True)
def tokens2json(ids, names, field, split, sep, token_docs):
    '''Convert a set of token documents into a
    JSON array of document objects.'''

    docs = []

    names = read_names(names)
    ids = read_names(ids)

    for idx, path in enumerate(token_docs):
        if path == '-':
            tokens_doc = sys.stdin
        else:
            tokens_doc = open(path, 'r')
        if split:
            content = read_csv(tokens_doc, sep)
            content = coerce_types(content)
        else:
            content = read_tokens(tokens_doc)

        # ordered so that these attributes stay at the top
        doc = OrderedDict()

        if idx < len(ids) - 1:
            doc['id'] = ids[idx]
        else:
            doc['id'] = path

        if idx < len(names) - 1:
            doc['name'] = names[idx]
        else:
            doc['name'] = path

        doc[field] = content
        docs.append(doc)
        tokens_doc.close()

    out_content = json.dumps(docs, indent=2)
    output(out_content)
