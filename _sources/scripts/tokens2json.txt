===========
tokens2json
===========

Description
===========

::

    Usage: textkit tokens2json [OPTIONS] [TOKEN_DOCS]...
    
      Convert a set of token documents into a JSON array of document objects.
    
    Options:
      --ids PATH            File with one id per token document, each separated by
                            a new line. Ids file is used to set the id attribute
                            in the output JSON.
      --names PATH          File with one name per token document, each separated
                            by a new line. Names file is used to set the name
                            attribute in the output JSON.
      --field TEXT          Attribute name where tokens will be stored in the
                            document object.  [default: tokens]
      --split / --no-split  If enabled, textkit will attempt to split input
                            columns when packaging. This is useful when packaging
                            multiple column output like counts.  [default: False]
      -s, --sep TEXT        Separator character between columns. Only used if
                            split-columns flag is used.  [default: ,]
      --help                Show this message and exit.
    


Examples
========
