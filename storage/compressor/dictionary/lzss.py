import ast
import re

from common import util


def append_limited(s, a, size):
    if len(s) < size:
        return s + a
    return s[1:] + a


def find_longest_match(window, buffer, min_match_size):
    longest_match = (-1, 0)
    for i in range(len(window)):
        for j in range(len(buffer)):
            if window[i + (j % (len(window) - i))] != buffer[j]:
                break
            if j+1 > longest_match[1] and j+1 >= min_match_size:
                longest_match = (i, j+1)
    return longest_match


def encode(text):
    min_match_size = 3
    max_match_size = 64
    window_size = 10240
    u = 1
    result = text[0]

    for _ in text[max_match_size:]:
        window = text[max(u-window_size, 0):u]
        buffer = text[u:u+max_match_size]
        match = find_longest_match(window, buffer, min_match_size)

        if match[0] == -1:
            if buffer:
                result += buffer[0]
            u += 1
        else:
            result += str(match)
            u += match[1]
    result += text[u:]
    return result


def compress(filename):
    text = util.load_file_as_text(filename)
    encoded = encode(text)
    encoded_bytes = encoded.encode()
    output = util.get_output_filename(filename)
    util.save_file_as_bytes(output, encoded_bytes)
    print(util.get_compression_ratio(encoded_bytes, text))


def decode(encoded_text):
    pattern = re.compile(r'^\(\d+, \d+\)')
    result = str()
    while encoded_text:
        if re.match(pattern, encoded_text):
            match = pattern.search(encoded_text).group()
            index, length = ast.literal_eval(match)
            for i in range(length):
                result += result[index + (i % (len(result) - index))]
            encoded_text = encoded_text[len(match):]
        else:
            result += encoded_text[0]
            encoded_text = encoded_text[1:]
    return result


def decompress(filename):
    encoded_bytes = util.load_file_as_byte(filename)
    encoded = encoded_bytes.decode()
    text = decode(encoded)
    output = util.get_original_filename(filename)
    util.save_file_as_text(output, text)
