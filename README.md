# textkit

Command line tools for text processing and analysis.


## About

`textkit` is a series of small, unix-style tools that provide a suite of capabilities for
dealing with text as data.

Think of textkit as basic natural language processing capabilities - from the command line.

## textkit Features

Here are some of the cool things you can do with textkit.

Convert a document to a set of word tokens and remove all punctuation from the tokens:

```
textkit text2words input.txt | textkit filterpunc
```

## Installation

To test locally, clone the repo:

```
git clone git@github.com:learntextvis/textkit.git
```

then use `pip` to install the repo in a local virtual environment or `conda` environment

```
cd textkit

pip install --editable .
```

_In the future:_

textkit is available via `pip`

```
pip install textkit
```

## Usage

textkit is an umbrella of commands all under the `textkit` command line tool.

```
textkit --help
```

Will show all the commands available. You can also get help on a particular command to see its arguments and options.

```
textkit text2words --help
```
