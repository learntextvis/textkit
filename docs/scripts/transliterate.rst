=============
transliterate
=============

Description
===========

::

    Usage: textkit transliterate [OPTIONS] [TEXT]...
    
      Transform an international text file to plain ascii
    
    Options:
      --help  Show this message and exit.
    


Examples
========

    > echo "Hello! À bientôt… L’été à Pètechïn; 日本語, Nihongo Klüft skräms inför på fédéral électoral große Küche Mærsk" > file_full_of_international_text.md
    > textkit transliterate file_full_of_international_text.md
    Hello! A bientot... L'ete a Petechin; Ri Ben Yu , Nihongo Kluft skrams infor pa federal electoral grosse Kuche Maersk