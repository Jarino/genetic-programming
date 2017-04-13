"""readcodetest"""

import unittest
import readcode


class ReadCodeTest(unittest.TestCase):
    """readcodetest"""

    def test_subtree_length(self):
        """Testujeme dlzku podstromu"""
        code = [2, 2, 0, 1, 0, 2, 1, 0, 2, 0, 0]
        length = readcode.subtree_length(code, 1)
        self.assertEqual(length, 4)

        length = readcode.subtree_length(code, 3)
        self.assertEqual(length, 2)

        length = readcode.subtree_length(code, 4)
        self.assertEqual(length, 1)

    def test_is_valid(self):
        """Rozne pripady kodov"""
        self.assertTrue(readcode.is_valid([0]))
        self.assertTrue(readcode.is_valid([1, 0]))
        self.assertTrue(readcode.is_valid([2, 0, 0]))
        self.assertTrue(readcode.is_valid([1, 1, 0]))
        self.assertFalse(readcode.is_valid([2, 1, 0]))
        self.assertTrue(readcode.is_valid([2, 1, 0, 0]))
        self.assertFalse(readcode.is_valid([2, 0, 0, 0]))
        self.assertFalse(readcode.is_valid([1, 2, 1, 0]))

    def test_code_generation(self):
        """Testujeme ci generovanie vytvori validny kod"""
        for i in range(1, 10):
            code = readcode.generate(i)
            self.assertTrue(readcode.is_valid(code))



if __name__ == '__main__':
    unittest.main()
