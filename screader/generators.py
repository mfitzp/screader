
from screader.formatters import markdown_formatters, is_valid_author, is_centered

import re

headerchars = re.compile(r'\s*([=+-]{5,})\s*')


def chunk(d, size=64):
    # Return data in chunk sizes.
    for i in range(0, len(d), size):
        yield d[i:i + size]


def plaintext_generator(data):
    """
    Process the decompressed data, dropping incomplete
    pages and stripping trailing whitespace on lines.
    """

    for n, line in enumerate(chunk(data)):
        line = line.decode('utf8')
        if len(line) != 64:
            break # skip final byte
                    
        yield line.rstrip() + '\n'


def markdown_generator(data):
    """
    Process the decompressed data to Markdown (generator).

    Uses formatters to attempt to generate sensible Markdown.    
    """
    last_title = None
    plines = []

    for n, line in enumerate(chunk(data)):
        line = line.decode('utf8')
            
        if len(line) != 64:
            break # skip final byte

        if headerchars.match(line):
            # line consists of Markdown header chars (--- or ====) only. Skip.
            continue
        
        if n % 21 == 0:
            # Possible page header line. Look for centered text
            # strip of the author, if present.
            # Find first space to strip author (for now).
            try:
                fs = line.index(' ')
            except ValueError:
                fs = 0
            author = line[:fs] if fs else ''
            sline = line[fs:]
            title = sline.strip()
            
            if title and is_valid_author(author) and is_centered(sline):
                # The text is centered, ish.                
                author = f' [{author}]' if author else ''
                
                if title != last_title:
                    # Markdown requires blank lines surrounding, ensure.
                    yield f'## {title}{author}\n\n'
                    last_title = title
                
                continue  # Skip the default handling.

        # For everything else, we need to process in blocks (paragraphs)
        # checking + dumping as we reach an empty line.
        if line.strip():
            # Store this line (para)
            plines.append(line)

        elif plines: 

            for condition, formatter in markdown_formatters:
                if condition(plines):
                    plines = formatter(plines)
                    break # as soon as we pass a condition, break out

            else:
                # We didn't hit a condition (no break).
                plines = [l.rstrip() for l in plines]


            # Dump the rows.
            for l in plines:
                yield l + '\n'
            
            # Yield the blank line itself.
            yield '\n'
            plines = []