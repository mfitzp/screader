def decompress(data, tokens):
    """
    Decompress source MAG data using run-length encoding and
    supplied token dictionary.
    """
    offset = int.from_bytes(data[0:2], byteorder='little') - 38233

    # If first 4 bytes contain values < 32 is version 1; skip 4 bytes
    if any(v < 32 for v in data[:4]):
        data = data[4:]

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
