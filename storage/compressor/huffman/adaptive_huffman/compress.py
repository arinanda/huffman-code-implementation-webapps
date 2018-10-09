from common import util
from huffman.adaptive_huffman.adaptive_huffman import *


def encode(text):
    encoded_text = str()
    root = None
    null = Node('null', 0)
    node_list = dict()
    for char in text:
        if char in node_list:
            encoded_text += get_code(node_list[char])
            node_list[char].value += 1
        else:
            encoded_text += get_code(null)
            encoded_text += '{0:08b}'.format(ord(char))
            node_list[char] = insert_node(null, char)
            if root is None:
                root = null.parent
        update_tree(null.parent)
    return encoded_text


def save(b, filename):
    with open(filename, 'wb') as output:
        output.write(b)


def compress(filename):
    text = util.load_file_as_text(filename)
    encoded_text = encode(text)
    encoded_bytes = util.to_byte_array(encoded_text)
    output = util.get_output_filename(filename)
    save(encoded_bytes, output)
    print(util.get_compression_ration(encoded_bytes, text))
