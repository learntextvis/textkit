import os
import click
import nltk
from textkit.utils import read_tokens, output


@click.command('download')
def download():
    '''
    Install required libraries.
    Note this library will install nltk dependencies into your
    user directory.
    '''

    click.echo("Installing nltk packages into your user directories in " +
               "the following order of existence (first found):\n" +
               '\n'.join(nltk.data.path))

    extensions = [("taggers", "averaged_perceptron_tagger"),
                  ("corpora", "wordnet")]

    missing = check_packages_exist(extensions)

    for ext_tuple in missing:
        nltk.download(ext_tuple[1])


def check_packages_exist(extensions):
    '''
    Finds missing nltk extensions.
    '''
    paths = nltk.data.path  # there are usually quite a few, so we check them all.
    missing = []
    ext_found = False
    for ext_tuple in extensions:
        click.echo(message="Looking for " + ext_tuple[1], nl=True)
        for path in paths:
            if os.path.exists(os.path.join(path, ext_tuple[0], ext_tuple[1])):
                ext_found = True
                click.echo(message="Found " + ext_tuple[1], nl=True)
                break
        if not ext_found:
            missing.append(ext_tuple)

    return missing
