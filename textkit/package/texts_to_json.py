import json
from collections import OrderedDict
import click
from textkit.utils import output, read_tokens

def read_names(names_path):
    names = []
    if names_path:
        names_doc = open(names_path, 'r')
        names = read_tokens(names_doc)
    return names


@click.command()
@click.argument('text_docs', type=click.Path(exists=True), nargs=-1)
@click.option('--ids', type=click.Path(),
              help="File with one id per text document, each separated by a " +
              "new line. Ids file is used to set the id attribute in the " +
              "output JSON.")
@click.option('--names', type=click.Path(),
              help="File with one name per text document, each separated " +
              "by a new line. Names file is used to set the name attribute " +
              "in the output JSON.")
@click.option('--field', default='text', help="Attribute name where text " +
              "will be stored in the document object.", show_default=True)

def texts2json(ids, names, field, text_docs):
    '''Convert a set of text documents into a
    JSON array of document objects.'''

    docs = []

    names = read_names(names)
    ids = read_names(ids)

    for idx, path in enumerate(text_docs):
        tokens_doc = open(path, 'r')
        content = ""
        with click.open_file(path):
            content = tokens_doc.read()

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
