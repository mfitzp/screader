import logging

def decompress(data, tokens):
    """
    Decompress source MAG data using run-length encoding and
    supplied token dictionary.
    """
    offset = int.from_bytes(data[0:2], byteorder='little') - 38233

    # If first 0th or 2nd bytes values < 32 is version 1.0 or v1.1;
    # this is quite horrible tbh.
    if any(v < 32 for v in data[:4:2]):
        logging.debug('Magazine file is v1.0 or v1.1.')

        number_of_articles = data[2]
        if number_of_articles == 0:
            logging.debug('Number of articles is zero, so v1.1.')
            # Version 1.1; skip 4 bytes.
            logging.debug('- strip first 4 bytes')
            data = data[4:]

        else:
            logging.debug('Number of articles is %d, so v1.0.', number_of_articles)
            # Version 1.0, we need to skip past the table.
            n = 5
            number_of_articles += 1  # Last entry is empty.
            while number_of_articles:
                n += 1
                if data[n] & 0x80:  # bit 7 is set.
                    number_of_articles -= 1

            logging.debug('- strip first %d bytes', n)
            data = data[n:]


    # Go through data, substituting.
    result = b''
    i = 0
    while i < len(data):
        byte = data[i]

        if byte == 128:
            # Run length compression, get another byte.
            i += 1
            length = data[i]
            result += b' ' * length
        else:
            char = tokens.get(
                byte,
                bytes([byte])
            ) # substitute if exists, fallback to existing.
            result += char #.decode('utf8')

        i += 1

    return result
