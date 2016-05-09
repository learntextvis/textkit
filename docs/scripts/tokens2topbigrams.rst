=================
tokens2topbigrams
=================

Description
===========

::

    b"Usage: textkit tokens2topbigrams [OPTIONS] [TOKENS]
    
      Find top most interesting bi-grams in a token document. Uses the --measure
      argument to determine what measure to use to define interesting.
    
    Options:
      -s, --sep TEXT                  Separator between tokens and scores in
                                      output.  [default: ,]
      -m, --measure [likelihood|chi_sq|pmi|student_t|freq]
                                      Specify which measure to use to define
                                      interesing-ness.  [default: likelihood]
      --freq INTEGER                  Minimum frequency of bi-grams to filter out.
                                      [default: 2]
      --scores / --no-scores          Include or exclude scores in output.
                                      [default: True]
      --help                          Show this message and exit.
    "


Examples
========
