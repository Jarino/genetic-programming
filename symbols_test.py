"""Module docstring"""

import unittest

import symbols

class SymbolsTest(unittest.TestCase):
    """test"""

    def test_assign_symbols(self):
        """Test priradenia symbolov"""
        code = [(2, None), (2, None), (1, None), (0, None), (0, None), (0, None)]
        assigned = symbols.assign_symbols(code)

        for tup in assigned:
            if tup[0] == 0:
                self.assertTrue(tup[1] in symbols.TERMINALS)
            if tup[0] == 1:
                self.assertTrue(tup[1] in symbols.UNARY)
            if tup[0] == 2:
                self.assertTrue(tup[1] in symbols.BINARY)

if __name__ == '__main__':
    unittest.main()
