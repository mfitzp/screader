# Sam Coupe *Entropy Reader* converter

This is a simple command-line converter for the Entropy Reader files, as used on the 
FRED disk magazine. The **DOCREADER** format uses a combination of run-length compression for whitespace and token compression for words to reduce the size of text files. The dictionary is fixed for a given version of the reader/compressor. The format is [documented here](http://simoncooke.com/samcoupe/infobase/docs/docreader.html).

Taking a MAG file and reader executable (or compressor version), this converter extracts the data from MAG files, converting them into plaintext and (optionally) attempting to generate sensible Markdown-formatted files.

If a reader executable is provided, the token table can be extracted automatically from it, and used for the decompression. Otherwise, the version of the compressor can be provided to use the built-in token tables. Special characters on the Sam are converted to Unicode equivalents.

The Markdown output performs a series of block-level guesses on content to try and produce sensible output. For example, on FRED the top line of each page was (often) used for a header with a title & the author, this is recognized and converted into Markdown headings (with the author in parentheses).
Blocks with visual formatting (a lot of internal whitespace) are recognised and rendered as fixed. Leading indentation on paragraphs is stripped. The conversion is pretty flaky, but it gets reasonable results.

Pass -s to skip the first instructions page (you probably always want to do this).

```
screader -h
usage: screader [-h] [--reader READER] [--readerversion {0,1,2}] [--skipinstructions] [--format {text,markdown}] [--outfile OUTFILE]
                mag [mag ...]

Extract Sam Coupe Entropy Reader files.

positional arguments:
  mag                   source MAG file(s) to process.

optional arguments:
  -h, --help            show this help message and exit
  --reader READER, -r READER
                        Path to the reader executable (token table will be extracted).
  --readerversion {0,1,2}, -rv {0,1,2}
                        Version of compressor token table to use (0, 1, 2 for v1.0, v1.1, v1.2 respectively).
  --skipinstructions, -s
                        Skip first page (instructions)
  --format {text,markdown}, -f {text,markdown}
                        Output format, one of (text, markdown).
  --outfile OUTFILE, -o OUTFILE
                        Output file (filename will be used for format, if not specified with -f. Output to stdout if not provided.)
```

Example Markdown output from Fred 29

```
## Chrissy Cards [CM]

ED's  NOTE:  Ha!  Look  at  that    ↑↑↑   - and he accuses ME of
leaving huge spaces!  What a nerve....                   - BRIAN

Thank  you  very  much for all the Christmas cards that everyone
sent  in. Things were too hectic to send any cards in return - I
apologize.  The  cards have long since been taken down but I can
remember  most  of  the  people  that  sent one in...but if I've
missed you out, I'm sorry :

    InterPrint         Pat Spencer               Stuart Burton
    Format             Derek & Maureen Morgan    PDC Copyprint
    ZAT Team           Stefan Drissen            Paul Jenkins
    Phil Glover        The Barnes-Lawrences      Chris Bailey
    Nicholas Bay       Andy Penny                Mairi Ross
    Mik Martin         Kevin Davies              Ian, Zeb & Morton Q
    Martin Scholes     Graham (0269)

Once  again,  a  belated Merry Christmas and a Happy New Year to
everyone - especially those listed above.
```
