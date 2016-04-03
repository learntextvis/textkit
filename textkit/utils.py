import os
import click
import sys


def read_tokens(file):
    '''Reads tokens from a file handle'''
    lines = file.readlines()
    return [l.rstrip('\n') for l in lines if len(l.rstrip('\n')) > 0]


def output(line):
    try:
        click.echo(line)
    except (OSError, IOError):
        sys.stderr.close()

def data_dir():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = "../data/"
    return os.path.abspath(os.path.join(current_directory, path))