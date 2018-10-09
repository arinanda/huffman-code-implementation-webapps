import os


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
    # return os.path.splitext(filename)[0]


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


def get_compression_ration(compressed, original):
    return (len(original) - len(compressed)) / len(original)
