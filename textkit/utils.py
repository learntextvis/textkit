import os
import click
import sys
import csv
from pkg_resources import resource_filename


def read_tokens(file):
    '''Reads tokens from a file handle'''
    lines = file.readlines()
    return [l.rstrip('\n') for l in lines if len(l.rstrip('\n')) > 0]


def read_csv(file, delim):
    '''Reads csv formated tokens from a file handle'''
    lines = []
    reader = csv.reader(file, delimiter=delim)
    lines = [line for line in reader]
    return lines


def write_csv(rows, delim):
    writer = csv.writer(click.get_text_stream('stdout'), delimiter=delim)
    try:
        [writer.writerow(row) for row in rows]
    except (OSError, IOError):
        sys.stderr.close()


def output(line):
    try:
        click.echo(line)
    except (OSError, IOError):
        sys.stderr.close()


def data_item(search_path=''):
    path = resource_filename(__name__, 'data/' + search_path)
    return path
