import unittest

from huffman.tunstall.compress import compress
from huffman.tunstall.decompress import decompress
from test import helper


class TunstallTestCase(unittest.TestCase):
    def test_tunstall(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
