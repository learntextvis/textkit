import click
import sys
import json
from textkit.utils import output, read_tokens
from textkit.coerce import coerce_types
from collections import OrderedDict


def read_names(names_path):
    names = []
    if(names_path):
        names_doc = open(names_path, 'r')
        names = read_tokens(names_doc)
    return names


@click.command()
@click.argument('token_docs', type=click.Path(), nargs=-1)
@click.option('--ids', type=click.Path(),
              help="File with one id per token document, each separated by a new line. Ids file is used to set the id attribute in the output JSON."
              )
@click.option('--names', type=click.Path(),
              help="File with one name per token document, each separated by a new line. Names file is used to set the name attribute in the output JSON."
              )
@click.option('--field', default='tokens', help="Attribute name where tokens will be stored in the document object.", show_default=True)
@click.option('--columns', default=1, help="Indicate how many columns are present in token rows. If more then one, textkit will attempt to produce JSON arrays for each row.", show_default=True)
@click.option('--sep', default=',', help="Separator character between columns. Only used if columns is greater then 1.", show_default=True)
def tokens2json(ids, names, field, columns, sep, token_docs):
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
        content = read_tokens(tokens_doc)

        # Split rows into columns
        if(columns > 1):
            content = [c.split(sep) for c in content]
            # attempt to coerce types
            content = coerce_types(content)

        # ordered so that these attributes stay at the top
        doc = OrderedDict()

        if(idx < len(ids) - 1):
            doc['id'] = ids[idx]
        else:
            doc['id'] = path

        if(idx < len(names) - 1):
            doc['name'] = names[idx]
        else:
            doc['name'] = path

        doc[field] = content
        docs.append(doc)
        tokens_doc.close()

    out_content = json.dumps(docs, indent=2)
    output(out_content)
