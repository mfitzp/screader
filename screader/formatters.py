
# Formatters for markdown

import re 

numeric = re.compile(r'^(\d+)[).;]')
internalspaces = re.compile(r'\w(\s{5,})\w')

def samcoupe_ascii_to_utf8(lines):
    for line in lines:
        line = (line
            .replace('\x5E', '↑') # is ^ by default, 
            .replace('\x5F', '_')
            .replace('\x60', '£')

            # .replace('\x7E', '~')
            .replace('\x7F', '©')
        )
        yield line


def is_valid_author(author):
    return ( 
        not author or len(author) == 2 and
        author == author.upper() 
    )


def is_centered(sline):
    leading = len(sline) - len(sline.lstrip())
    trailing = len(sline) - len(sline.rstrip())
    return leading > 1 and abs(trailing-leading) < 10   


def only_first_indented(lines):
    first_line = lines[0]
    return (
        len(first_line.lstrip()) < len(first_line) and 
        all(len(l.lstrip()) == len(l) for l in lines[1:])
        )


def all_indented(lines):
    n_lines = len(lines)
    n_indented = sum(len(l.lstrip()) < len(l) for l in lines)
    return n_lines == n_indented    


def mostly_indented(lines):
    n_lines = len(lines)
    n_indented = sum(len(l.lstrip()) < len(l) for l in lines)
    return n_indented > n_lines / 2 and n_indented < n_lines # More than 1/2 indented, but not all


def numeric_list(lines):
    n_lines = len(lines)
    numeric_lines = sum(numeric.search(l) is not None for l in lines)
    return (
        numeric_lines == n_lines or 
        (
            numeric_lines > 0 and 
            all(
                numeric.search(l) is not None or # starts with a formatted digit.
                len(l.lstrip()) < len(l)  # indented
                for l in lines
                )
        )
    )


def contains_visual_alignment(lines):
    lines_with_whitespace = sum(internalspaces.search(l) is not None for l in lines)
    return (lines_with_whitespace > len(lines) / 2) and not all_indented(lines)


def short_lines(lines):
    return all(len(l) < 64 for l in lines)


def single_line_centered(lines):
    return len(lines) == 1 and is_centered(lines[0])


def unindent_first_line(lines):
    lines[0] = lines[0].lstrip()
    return lines


def indent_all_lines(lines):
    return [f'    {l.strip()}' for l in lines]
            

def markdown_header(lines):
    header = lines[0].strip()
    return [f'## {header}\n']    


def markdown_numbered_list(lines):
    return [numeric.sub(r'\1.', l.strip()) for l in lines]    


def markdown_hard_wrap_lines(lines):
    return [f'{l.rstrip()}  ' for l in lines]


# Checks and formatters for Markdown.
markdown_formatters = [
    (single_line_centered, markdown_header),
    (only_first_indented, unindent_first_line),
    (numeric_list, markdown_numbered_list),
    (contains_visual_alignment, indent_all_lines),
    (mostly_indented, indent_all_lines),
    (short_lines, markdown_hard_wrap_lines),
]