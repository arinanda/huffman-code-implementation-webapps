from collections import defaultdict
from heapq import heappush, heappop

from common import util
from common.util import Node


def calc_freq(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq


def make_heap(freq):
    heap = list()
    for char, freq in freq.items():
        heappush(heap, Node(char, freq))
    return heap


def build_tree(heap):
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        heappush(heap, Node(None, left.value + right.value, None, left, right))
    return heap[0]


def assign_codes(codes, node, code=str()):
    if node is not None:
        if node.char is not None:
            codes[node.char] = code
            return
        assign_codes(codes, node.left, code + "0")
        assign_codes(codes, node.right, code + "1")


def build_codes(root):
    codes = dict()
    assign_codes(codes, root)
    return codes


def encode(codes, text):
    encoded_text = str()
    for char in text:
        encoded_text += codes[char]
    return encoded_text


def save(b, codes, filename):
    with open(filename, 'wb') as output:
        output.write(str(codes).encode())
        output.write('\n'.encode())
        output.write(b)


def compress(filename):
    text = util.load_file_as_text(filename)
    freq = calc_freq(text)
    heap = make_heap(freq)
    root = build_tree(heap)
    codes = build_codes(root)
    encoded_text = encode(codes, text)
    encoded_bytes = util.to_byte_array(encoded_text)
    output = util.get_output_filename(filename)
    save(encoded_bytes, codes, output)
    print(util.get_compression_ratio(encoded_bytes, text))
