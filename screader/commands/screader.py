import os

import re
import argparse

from screader.tokens import build_token_dictionary, TOKENSV10, TOKENSV12
from screader.decompress import decompress

from screader.generators import markdown_generator, plaintext_generator
from screader.formatters import samcoupe_ascii_to_utf8


parser = argparse.ArgumentParser(description='Extract Sam Coupe Entropy Reader files.')
parser.add_argument('mag', type=str, nargs='+',
                    help='source MAG file(s) to process.')

parser.add_argument('--reader', '-r', type=str, help='Path to the reader executable (token table will be extracted).')
parser.add_argument('--readerversion', '-rv', type=int, choices=[0,1,2], help='Version of compressor token table to use (0, 1, 2 for v1.0, v1.1, v1.2 respectively).')

parser.add_argument('--skipinstructions', '-s', default=False, action='store_const', const=True, help='Skip first page (instructions)')

parser.add_argument('--format', '-f', type=str, choices=['text','markdown'], default='text', help='Output format, one of (text, markdown).')

parser.add_argument('--outfile', '-o', type=str, help='Output file (filename will be used for format, if not specified with -f. Output to stdout if not provided.)')




def main():

    args = parser.parse_args()

    tokens = None
    if args.reader:
        
        with open(args.reader, 'rb') as f:
            data = f.read()
        
        tokens = build_token_dictionary(data)
    
    elif args.readerversion:
        tokens = {
            0:TOKENSV10,
            1:TOKENSV10,
            2:TOKENSV12,
        }.get(args.readerversion)

    if tokens is None:
        print("Error: No token table, provide a valid doc reader executable or specify reader version.")
        exit(1)

    # Get the formatter specified, falling back to plaintext.
    formatter, ext = {
        'text': (plaintext_generator, '.txt'),
        'plaintext': (plaintext_generator, '.txt'),
        'markdown': (markdown_generator, '.md')

    }.get(args.format, (plaintext_generator, '.txt'))

    if len(args.mag) > 1 and args.outfile:
        print("Cannot specify output filename when processing multiple files.")
        exit(1)

    for magfilename in args.mag:

        basename = os.path.basename(magfilename)
        filename, _ = os.path.splitext(basename)

        # Load up the mag file.
        with open(magfilename, 'rb') as f:
            data = f.read()

        result = decompress(data, tokens)

        if args.skipinstructions:
            # Skip the first page (instructions)
            result = result[1344:]

        # Process the data to lines using the formatter.
        lines = formatter(result)
        lines = samcoupe_ascii_to_utf8(lines)

        if args.outfile:
            outfile = args.outfile

        else:
            outfile = f'{filename}{ext}'

        with open(outfile, 'w') as f:
            f.writelines(lines)









