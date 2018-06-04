import sys, unicodedata

USAGE = "usage: {prog} [--help] < INPUT > OUTPUT"

HELP = """The program reads UTF-8 text from stdin and writes to stdout information
about each character, one per line.
The output has 5 tab-separated columns:
    1 - the character itself, if printable, or an escaped representation of it
    2 - the decimal codepoint of the character
    3 - the number of bytes that the character occupies
    4 - the Unicode category of the character
    5 - the Unicode name of the character
"""


if __name__ == "__main__":
    main()


def main():
    if len(sys.argv) == 2 and sys.argv[1] in ["--help", "-h", "-?"]:
        print(HELP)
        sys.exit(0)

    if len(sys.argv) > 1:
        print(USAGE.format(prog=sys.argv[0]), file=sys.stderr)
        sys.exit(1)
    
    replace = {
        '\n': '\\n',
        '\t': '\\t',
        '\v': '\\v',
        '\b': '\\b',
        '\f': '\\f',
        '\a': '\\a',
        '\\': '\\\\',
    }

    for line in sys.stdin:
        for c in line:
            cat = unicodedata.category(c)
            name = unicodedata.name(c, '') if c != '\n' else 'NEWLINE'
            octets = len(bytes(c, 'utf-8'))
            print(replace.get(c, c), ord(c), octets, cat, name, sep='\t')
