uctools
=======

Tools for showing information about unicode characters (UTF-8).

Copyright ® 2018, Luís Gomes <luismsgomes@gmail.com>.

The following command line tools are provided:

    ucinfo
        writes on stdout the name of each unicode character read from stdin

    ucenum
        enumerates on stdout all unicode characters of a chosen category

ucinfo
------

The ucinfo tool reads UTF-8 text from stdin and writes to stdout information
about each character, one per line.
The output has 5 tab-separated columns:

    1. the character itself, if printable, or an escaped representation of it
    2. the decimal codepoint of the character
    3. the number of bytes that the character occupies
    4. the Unicode category of the character
    5. the Unicode name of the character

ucenum
------

The ucenum tool takes a category abbreviation as argument and outputs a list
 of all characters belonging to that category.  The categories are:

    L
        Letter
    Lu
        Letter, Uppercase
    Ll
        Letter, Lowercase
    Lt
        Letter, Titlecase
    Lm
        Letter, Modifier
    Lo
        Letter, Other
    M
        Mark
    Mn
        Mark, Nonspacing
    Mc
        Mark, Spacing Combining
    Me
        Mark, Enclosing
    N
        Number
    Nd
        Number, Decimal Digit
    Nl
        Number, Letter
    No
        Number, Other
    P
        Punctuation
    Pc
        Punctuation, Connector
    Pd
        Punctuation, Dash
    Ps
        Punctuation, Open
    Pe
        Punctuation, Close
    Pi
        Punctuation, Initial quote (may behave like Ps or Pe depending on usage)
    Pf
        Punctuation, Final quote (may behave like Ps or Pe depending on usage)
    Po
        Punctuation, Other
    S
        Symbol
    Sm
        Symbol, Math
    Sc
        Symbol, Currency
    Sk
        Symbol, Modifier
    So
        Symbol, Other
    Z
        Separator
    Zs
        Separator, Space
    Zl
        Separator, Line
    Zp
        Separator, Paragraph
    C
        Other
    Cc
        Other, Control
    Cf
        Other, Format
    Cs
        Other, Surrogate
    Co
        Other, Private Use
    Cn
        Other, Not Assigned