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
