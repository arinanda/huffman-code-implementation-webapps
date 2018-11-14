import ast
import struct

from common import util


def extract(compressed_text):
    ln, ranges, encoded_bytes = compressed_text.split(b'\n', 2)
    ln = int(ln.decode())
    ranges = ast.literal_eval(ranges.decode())
    return ln, ranges, encoded_bytes


def decode(encoded_value, ln, ranges):
    decoded_text = str()
    lower = 0.0
    upper = 1.0

    for i in range(ln):
        width = upper - lower
        for k, v in ranges.items():
            lo = lower + width * v[0]
            hi = lower + width * v[1]
            if lo < encoded_value < hi:
                decoded_text += k
                lower = lo
                upper = hi
                break

    return decoded_text


def save(text, filename):
    with open(filename, 'wt') as output:
        output.write(text)


def decompress(filename, chars=None, probs=None):
    compressed_text = util.load_file_as_byte(filename)
    ln, ranges, encoded_bytes = extract(compressed_text)
    encoded_value = struct.unpack('f', encoded_bytes)[0]
    print(encoded_value)
    decoded_text = decode(encoded_value, ln, ranges)
    output = util.get_original_filename(filename)
    save(decoded_text, output)
