import unittest

from arithmetic.compress import compress
from arithmetic.decompress import decompress
from test import helper


class ArithmeticTestCase(unittest.TestCase):
    def test_arithmetic(self):
        self.assertTrue(helper.coding_test(compress, decompress))


if __name__ == '__main__':
    unittest.main()
