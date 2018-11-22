import unittest

from dictionary.lzss import compress, decompress
from test import helper


class LZSSTestCase(unittest.TestCase):
    def test_lzss(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
