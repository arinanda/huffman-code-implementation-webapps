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


def build_code(probs, n):
    size = len(probs)
    iterations = (2 ** n - size) // (size - 1)
    symbols = probs.keys()

    while iterations > 0:
        char, char_prob = max(probs, key=lambda k: probs[k])

        for s in symbols:
            probs[char + s] = char_prob * probs[s]
        del probs[char]

    for i, k in enumerate(probs):
        probs[k] = '{:03b}'.format(i)
    return probs


def encode(text, code):
    encoded_text = str()
    current_text = str()
    for char in text:
        current_text += char
        if current_text in code:
            encoded_text += code[current_text]
            current_text = str()
    return encoded_text


def save(b, codes, filename):
    with open(filename, 'wb') as output:
        output.write(str(codes).encode())
        output.write('\n'.encode())
        output.write(b)


def compress(filename, n=4):
    text = util.load_file_as_text(filename)
    probs = calc_prob(text)
    codes = build_code(probs, n)
    encoded_text = encode(text, codes)
    encoded_bytes = util.to_byte_array(encoded_text)
    output = util.get_output_filename(filename)
    save(encoded_bytes, codes, output)
    print(util.get_compression_ration(encoded_bytes, text))
