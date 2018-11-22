import unittest

from huffman.huffman.compress import compress
from huffman.huffman.decompress import decompress
from test import helper


class HuffmanTestCase(unittest.TestCase):
    def test_huffman(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
