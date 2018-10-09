import ast

from common import util


def extract(compressed_text):
    codes, encoded_bytes = compressed_text.split(b'\n', 1)
    codes = ast.literal_eval(codes.decode())
    codes = {v: k for k, v in codes.items()}
    return codes, encoded_bytes


def to_bitstring(padded_encoded_bytes):
    return ''.join(['{0:08b}'.format(bit) for bit in padded_encoded_bytes])


def remove_padding(padded_encoded_text):
    padding_info = padded_encoded_text[:8]
    padding_length = int(padding_info, 2)
    return padded_encoded_text[8:-padding_length]


def decode(encoded_text, codes):
    decoded_text = str()
    current_code = str()
    for bit in encoded_text:
        current_code += bit
        if current_code in codes:
            decoded_text += codes[current_code]
            current_code = str()
    return decoded_text


def save(text, filename):
    with open(filename, 'wt') as output:
        output.write(text)


def decompress(filename):
    compressed_text = util.load_file_as_byte(filename)
    codes, encoded_bytes = extract(compressed_text)
    encoded_text = util.to_bitstring(encoded_bytes)
    text = decode(encoded_text, codes)
    output = util.get_original_filename(filename)
    save(text, output)
