import unittest

from common import util


class UtilTestCase(unittest.TestCase):
    bookkeeper = 'test/files/bookkeeper'

    def test_load_file(self):
        self.assertEqual('bookkeeper', util.load_file(self.bookkeeper, 't'))
        self.assertEqual(b'bookkeeper', util.load_file(self.bookkeeper, 'b'))

    def test_load_file_as_text(self):
        self.assertEqual('bookkeeper', util.load_file_as_text(self.bookkeeper))

    def test_load_file_as_byte(self):
        self.assertEqual(b'bookkeeper', util.load_file_as_byte(self.bookkeeper))

    def test_get_output_filename(self):
        self.assertEqual(self.bookkeeper + '.output', util.get_output_filename(self.bookkeeper))

    def test_get_output_filename_with_extension(self):
        self.assertEqual(self.bookkeeper + '.ext', util.get_output_filename(self.bookkeeper, 'ext'))

    def test_get_original_filename(self):
        self.assertEqual(self.bookkeeper, util.get_original_filename(self.bookkeeper + '.output'))

    def test_padding(self):
        b = util.add_padding(self.bookkeeper)
        self.assertEqual(self.bookkeeper, util.remove_padding(b))

    def test_byte_array_conversion(self):
        text = '100'
        b = util.to_byte_array(text)
        self.assertEqual(text, util.to_bitstring(b))

    def test_get_compression_ration(self):
        self.assertLess(0.610, util.get_compression_ratio('x' * 611, 'x' * 1000))
        self.assertGreater(0.612, util.get_compression_ratio('x' * 611, 'x' * 1000))

    def test_calc_freq(self):
        self.assertDictEqual({'a': 1, 'b': 1}, util.calc_freq('ab'))

    def test_calc_prob(self):
        self.assertDictEqual({'a': 0.5, 'b': 0.5}, util.calc_prob('ab'))


if __name__ == '__main__':
    unittest.main()
