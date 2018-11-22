import unittest

from dictionary.lzw import compress, decompress
from test import helper


class LZWTestCase(unittest.TestCase):
    def test_lzw(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
