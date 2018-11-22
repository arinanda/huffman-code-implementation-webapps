import unittest

from huffman.adaptive_huffman.compress import compress
from huffman.adaptive_huffman.decompress import decompress
from test import helper


class AdaptiveHuffmanTestCase(unittest.TestCase):
    def test_adaptive_huffman(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
