import struct
from collections import defaultdict

from common import util


def calc_freq(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq


def calc_prob(text):
    freq = calc_freq(text)
    prob = dict(map(lambda k: (k, freq[k] / len(text)), freq))
    return prob


def calc_range(freq):
    ranges = dict()
    lower = 0
    for k in freq:
        ranges[k] = (lower, lower + freq[k])
        lower += freq[k]
    return ranges


def encode(text, ranges):
    lower = 0.0
    upper = 1.0

    for c in text:
        if c in ranges:
            width = upper - lower
            l, u = ranges[c]
            upper = lower + width * u
            lower = lower + width * l

    return (lower + upper) / 2.0


def save(b, ranges, ln, filename):
    with open(filename, 'wb') as output:
        output.write(str(ln).encode())
        output.write('\n'.encode())
        output.write(str(ranges).encode())
        output.write('\n'.encode())
        output.write(b)


def compress(filename, chars, probs):
    text = util.load_file_as_text(filename)
    probs = {chars.split(',')[i]: float(probs.split(',')[i]) for i in range(len(probs.split(',')))}
    ranges = calc_range(probs)
    encoded_value = encode(text, ranges)
    encoded_bytes = bytearray(struct.pack("f", encoded_value))
    output = util.get_output_filename(filename)
    save(encoded_bytes, ranges, len(text), output)
    print(util.get_compression_ration(encoded_bytes, text))
