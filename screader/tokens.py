

# Pre-built tokens for each version of docreader (taken from Fred issues 17, 28)
# V10 & V11 tokens from Fred 28 DOCREADER.
TOKENSV10 = {129: b'address ', 130: b'screens ', 131: b'screen ', 132: b' issue ', 133: b'memory ', 134: b'screen ', 135: b" don't ", 136: b' SAMCO ', 137: b' SAMCo ', 138: b'Coupe ', 139: b' FRED ', 140: b'bytes ', 141: b' data ', 142: b" it's ", 143: b' from ', 144: b' SAM ', 145: b'\x7f 199', 146: b'code ', 147: b'Code ', 148: b'Data ', 149: b'ould ', 150: b' out ', 151: b' had ', 152: b'Coupe', 153: b'SAMCO', 154: b'SAMCo', 155: b'The ', 156: b'the ', 157: b'tion', 158: b' at ', 159: b'empt', 160: b'\x7f199', 161: b'comp', 162: b'Comp', 163: b'cons', 164: b'Cons', 165: b'... ', 166: b' you', 167: b"'ll ", 168: b'ere ', 169: b'You ', 170: b' it ', 171: b'.) ', 172: b"n't", 173: b'ity', 174: b'At ', 175: b'199', 176: b'ing', 177: b'een', 178: b'and', 179: b'And', 180: b'ght', 181: b'mag', 182: b'pro', 183: b'oum', 184: b'ove', 185: b'age', 186: b' - ', 187: b"'m ", 188: b"'s ", 189: b'You', 190: b' I ', 191: b'ant', 192: b'ial', 193: b'   ', 194: b' (', 195: b'er', 196: b', ', 197: b'  ', 198: b'. ', 199: b'! ', 200: b'? ', 201: b'A ', 202: b'or', 203: b'ss', 204: b'ee', 205: b'ch', 206: b'sh', 207: b'un', 208: b'ly', 209: b'th', 210: b'Th', 211: b'To', 212: b'to', 213: b'ow', 214: b'qu', 215: b'Qu', 216: b'Be', 217: b'be', 218: b'Up', 219: b'up', 220: b'Re', 221: b're', 222: b'en', 223: b'En', 224: b'us', 225: b'Us', 226: b'ed', 227: b'oo', 228: b'."', 229: b'!"', 230: b'?"', 231: b'; ', 232: b': ', 233: b') ', 234: b'pe', 235: b'Pe', 236: b'ir', 237: b'Ir', 238: b'my', 239: b'pp', 240: b'I ', 241: b'dd', 242: b'ea', 243: b'ff', 244: b'ss', 245: b'it', 246: b'rr', 247: b'at', 248: b'At', 249: b'e ', 250: b'y ', 251: b'ic'}
TOKENSV12 = {129: b"you'll", 130: b'ould', 131: b'ouse', 132: b'cons', 133: b'comp', 134: b"I'll", 135: b'entr', 136: b'ight', 137: b'   ', 138: b'ent', 139: b'ing', 140: b'out', 141: b'ang', 142: b'cei', 143: b'ial', 144: b'ant', 145: b'mag', 146: b'pro', 147: b'age', 148: b"I'm", 149: b"'ll", 150: b'had', 151: b"n't", 152: b'ean', 153: b'eem', 154: b'ove', 155: b"I'd", 156: b'een', 157: b'all', 158: b'oup', 159: b'SAM', 160: b'the', 161: b'The', 162: b'dis', 163: b'key', 164: b'ave', 165: b'opy', 166: b'oil', 167: b'air', 168: b'eer', 169: b'ure', 170: b'ion', 171: b'vis', 172: b'ban', 173: b'mon', 174: b'hor', 175: b'ard', 176: b'ish', 177: b'nal', 178: b'  ', 179: b'. ', 180: b', ', 181: b"'s", 182: b'om', 183: b'sh', 184: b'ch', 185: b'ew', 186: b'ng', 187: b'ic', 188: b'tr', 189: b'cr', 190: b'it', 191: b'ff', 192: b'ss', 193: b'ee', 194: b'oo', 195: b'ou', 196: b'ie', 197: b'ei', 198: b"'m", 199: b'nt', 200: b'fl', 201: b'ph', 202: b'qu', 203: b'be', 204: b'up', 205: b're', 206: b'en', 207: b'us', 208: b'ed', 209: b'to', 210: b'ow', 211: b'rr', 212: b'ea', 213: b'ar', 214: b'pe', 215: b'mu', 216: b'th', 217: b'Th', 218: b'll', 219: b'ff', 220: b'In', 221: b'in', 222: b'pp', 223: b'my', 224: b'I ', 225: b'or', 226: b'on', 227: b'et', 228: b'sc', 229: b'ut', 230: b'ex', 231: b'ce', 232: b'ck', 233: b'at', 234: b'At', 235: b'A ', 236: b'a ', 237: b'It', 238: b'is', 239: b'Is', 240: b'su', 241: b'Co', 242: b'er', 243: b'de', 244: b'di', 245: b'bi', 246: b'ey', 247: b'sp', 248: b'go', 249: b'aw', 250: b'ay', 251: b'il', 252: b'op', 253: b'an', 254: b'oc', 255: b'id'}

# The following sequence precedes/follows the table in V10/V12, not an actual 'marker' but works.
TOKENSV10_MARKER = (b'\x8D\x01\x8F\x01\x91\x01\x93\x01\x95\x01', b'<<<<<')
TOKENSV12_MARKER = (b'\x2F\x01\x31\x01\x33\x01\x35\x01\x37\x01', b'<<<<<')

def get_token_dictionary(data):
    for before, after in [TOKENSV10_MARKER, TOKENSV12_MARKER]:
        try:
            start = data.index(before)
            end = data.index(after)
            if start and end:
                start += len(before)
                return data[start:end]
        except ValueError:
            pass
    else:
        raise Exception("Token dictionary table not found.")
    

def build_token_dictionary(data):
    """
    Build a token dictionary from the supplied docread binary.
    Works for v1.0, v1.1 and v1.2 doc readers.
    """
    # data is bytestring, isolate substitutions (byte 918 onwards)
    data = get_token_dictionary(data)
    tokenix = 129 # tokens start at 129.
    tokens = {}
    token = b''
    i = 0
    while i < len(data):
        
        byte = data[i]

        if byte & 0x80:
            # High bit set, subtract, store, and get ready for next token.
            byte -= 0x80
            token += bytes([byte])
            tokens[tokenix] = token
            tokenix += 1
            token = b''
        else:
            token += bytes([byte])
        
        i += 1
    return tokens