import string

from common import util


def encode(text):
    dictionary = {c: i for i, c in enumerate(string.ascii_letters + string.digits)}
    result = []
    w = ''
    for c in text:
        if w + c in dictionary:
            w += c
        else:
            result.append(dictionary[w])
            dictionary[w+c] = len(dictionary)
            w = c
    result.append(dictionary[w])
    return result


def compress(filename):
    text = util.load_file_as_text(filename)
    encoded_values = encode(text)
    encoded_bytes = bytes(encoded_values)
    output = util.get_output_filename(filename)
    util.save_file_as_bytes(output, encoded_bytes)
    print(util.get_compression_ratio(encoded_bytes, text))


def decode(encoded_values):
    dictionary = list(string.ascii_letters + string.digits)
    w = dictionary[encoded_values[0]]
    result = w
    for v in encoded_values[1:]:
        if v < len(dictionary):
            out = dictionary[v]
        elif v == len(dictionary):
            out = w + w[0]
        else:
            out = None
        result += out
        dictionary.append(w + out[0])
        w = out
    return result


def decompress(filename):
    encoded_bytes = util.load_file_as_byte(filename)
    encoded_values = list(encoded_bytes)
    text = decode(encoded_values)
    output = util.get_original_filename(filename)
    util.save_file_as_text(output, text)
