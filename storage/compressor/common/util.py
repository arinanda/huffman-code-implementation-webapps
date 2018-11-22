import ast
import os
from collections import defaultdict


class Compressor:
    extension = 'output'

    def compress(self, filename):
        text = load_file_as_text(filename)
        encoded = self.encode(text, **self.get_encoding_args(text))
        encoded_bytes = self.get_encoded_bytes(encoded)
        save_file_as_bytes(get_output_filename(filename, self.extension), encoded_bytes)
        print(get_compression_ratio(encoded_bytes, text))

    def get_encoding_args(self, text):
        return {}

    def encode(self, text, **kwargs):
        return text

    def get_encoded_bytes(self, encoded):
        return encoded


class Node:
    def __init__(self, char=None, value=0, parent=None, left=None, right=None):
        self.char = char
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __lt__(self, other):
            return self.value < other.value

    def __str__(self):
        return '%s:%s' % (self.char, self.value)


def load_file(filename, mode):
    with open(filename, 'r' + mode) as file:
        return file.read()


def load_file_as_text(filename):
    return load_file(filename, 't')


def load_file_as_byte(filename):
    return load_file(filename, 'b')


def get_output_filename(filename, extension='output'):
    filename, _ = os.path.splitext(filename)
    return '%s.%s' % (filename, extension)


def get_original_filename(filename):
    return get_output_filename(filename)


def to_byte_array(text):
    text = add_padding(text)
    b = bytearray()
    for i in range(0, len(text), 8):
        b.append(int(text[i:i+8], 2))
    return b


def add_padding(encoded_text):
    padding_length = 8 - (len(encoded_text) % 8)
    padding = '0' * padding_length
    padding_info = '{0:08b}'.format(padding_length)
    encoded_text = padding_info + encoded_text + padding
    return encoded_text


def to_bitstring(padded_encoded_bytes):
    padded_encoded_bytes = ''.join(['{0:08b}'.format(bit) for bit in padded_encoded_bytes])
    return remove_padding(padded_encoded_bytes)


def remove_padding(padded_encoded_text):
    padding_info = padded_encoded_text[:8]
    padding_length = int(padding_info, 2)
    return padded_encoded_text[8:-padding_length]


def get_compression_ratio(compressed, original):
    return len(compressed) / len(original)


def calc_freq(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return {k: freq[k] for k in sorted(freq)}


def calc_prob(text):
    freq = calc_freq(text)
    prob = dict(map(lambda k: (k, freq[k] / len(text)), freq))
    return prob


def save_file(filename, mode, output):
    with open(filename, mode) as out_file:
        out_file.write(output)


def save_file_as_text(filename, output_text):
    save_file(filename, 'wt', output_text)


def save_file_as_bytes(filename, output_bytes):
    save_file(filename, 'wb', output_bytes)
