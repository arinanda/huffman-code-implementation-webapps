from common import util
from huffman.adaptive_huffman.adaptive_huffman import *


def check_code(root, code):
    for i in range(1, len(code)):
        if root:
            if code[i] == '0':
                root = root.left
            else:
                root = root.right
    return root.char if root else None


def decode(encoded_text):
    decoded_text = str()
    root = null = Node('null', 0)
    node_list = dict()
    current_code = str()
    i = 0
    while i < len(encoded_text):
        current_code += encoded_text[i]
        i += 1
        try_code = check_code(root, current_code)
        if try_code:
            if try_code == 'null':
                new_char = str(chr(int(encoded_text[i:i+8], 2)))
                node_list[new_char] = insert_node(null, new_char)
                if root is null:
                    root = null.parent
                decoded_text += new_char
                i += 8
            else:
                decoded_text += try_code
                node_list[try_code].value += 1
            current_code = str()
            update_tree(null.parent)
    return decoded_text


def save(text, filename):
    with open(filename, 'wt') as output:
        output.write(text)


def decompress(filename):
    encoded_bytes = util.load_file_as_byte(filename)
    encoded_text = util.to_bitstring(encoded_bytes)
    text = decode(encoded_text)
    output = util.get_original_filename(filename)
    save(text, output)
