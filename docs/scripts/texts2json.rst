==========
texts2json
==========

Description
===========

::

    Usage: textkit texts2json [OPTIONS] [TEXT_DOCS]...
    
      Convert a set of text documents into a JSON array of document objects.
    
    Options:
      --ids PATH    File with one id per text document, each separated by a new
                    line. Ids file is used to set the id attribute in the output
                    JSON.
      --names PATH  File with one name per text document, each separated by a new
                    line. Names file is used to set the name attribute in the
                    output JSON.
      --field TEXT  Attribute name where text will be stored in the document
                    object.  [default: text]
      --help        Show this message and exit.
    


Examples
========
