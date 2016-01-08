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
textkit text2words input.txt | textkit filterpunc -
```

Count top used words in a text:

```
textkit text2words alice.txt | textkit count - | head
```

Do the same, but with punctuation removed:

```
textkit text2words alice.txt | textkit filterpunc - | textkit count - | head
```

## Installation

To test locally, clone the repo:

```
git clone git@github.com:learntextvis/textkit.git
```

Create a local virtual environment or `conda` environment.

Here is how I created my local `conda` environment for installing and testing textkit:

```
conda create -name textkit nltk

source activate textkit
```

Then I went into the `textkit` directory to install its requirements

```
cd textkit

pip install -r requirements.txt
```

Finally, I installed the local version of textkit using the `--editable` flag:

```
pip install --editable .
```

_In the future basic installation instructions will be just the following:_

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

Chaining of textkit commands is possible (and encouraged) with unix pipes (`|`). Use the dash `-` to indicate the output of a previous command should be used as input for the next command.
