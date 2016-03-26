import click
import sys
import csv


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


def output(line):
    try:
        click.echo(line)
    except (OSError, IOError):
        sys.stderr.close()
