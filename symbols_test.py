"""Module docstring"""

import unittest

import symbols

class SymbolsTest(unittest.TestCase):
    """test"""

    def test_assign_symbols(self):
        """Test priradenia symbolov"""
        code = [(3, None), (2, None), (1, None), (0, None), (0, None), (0, None)]
        assigned = symbols.assign_symbols(code)

        for tup in assigned:
            if tup[0] == 0:
                self.assertTrue(tup[1] in symbols.TERMINALS)
            else:
                self.assertTrue(tup[1] in symbols.NONTERMINALS)

if __name__ == '__main__':
    unittest.main()
