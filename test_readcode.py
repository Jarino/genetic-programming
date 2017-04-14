"""readcodetest"""

import unittest
import readcode


class ReadCodeTest(unittest.TestCase):
    """readcodetest"""

    def test_subtree_length(self):
        """Testujeme dlzku podstromu"""
        code = [(2, 'a'), (2, 'a'), (0, 'a'), (1, 'a'),
                (0, 'a'), (2, 'a'), (1, 'a'), (0, 'a'),
                (2, 'a'), (0, 'a'), (0, 'a')]
        length = readcode.subtree_length(code, 1)
        self.assertEqual(length, 4)

        length = readcode.subtree_length(code, 3)
        self.assertEqual(length, 2)

        length = readcode.subtree_length(code, 4)
        self.assertEqual(length, 1)

    def test_is_valid(self):
        """Rozne pripady kodov"""
        self.assertTrue(readcode.is_valid([(0, 'a')]))
        self.assertTrue(readcode.is_valid([(1, 'a'), (0, 'a')]))
        self.assertTrue(readcode.is_valid([(2, 'a'), (0, 'a'), (0, 'a')]))
        self.assertTrue(readcode.is_valid([(1, 'a'), (1, 'a'), (0, 'a')]))
        self.assertFalse(readcode.is_valid([(2, 'a'), (1, 'a'), (0, 'a')]))
        self.assertTrue(readcode.is_valid([(2, 'a'), (1, 'a'), (0, 'a'), (0, 'a')]))
        self.assertFalse(readcode.is_valid([(2, 'a'), (0, 'a'), (0, 'a'), (0, 'a')]))
        self.assertFalse(readcode.is_valid([(1, 'a'), (2, 'a'), (1, 'a'), (0, 'a')]))

    def test_code_generation(self):
        """Testujeme ci generovanie vytvori validny kod"""
        for i in range(1, 10):
            code = readcode.generate(i)
            print(code)
            self.assertTrue(readcode.is_valid(code))

    def test_parsing(self):
        """Testujeme parsovanie kodu do matematickeho vyrazu"""
        code = [(2, '+'), (2, '-'), (1, 'sin'), (2, '+'), (0, 'x'), (0, 'x'), (0, 'y'), (0, 'z')]
        res = readcode.parse(code)
        self.assertEqual(res, '(((sin((x+x)))-y)+z)')

if __name__ == '__main__':
    unittest.main()
