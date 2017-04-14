"""genetic operations tests"""
import unittest
import readcode
import genetic_operations

class GeneticOperationsTest(unittest.TestCase):
    """another useless docstring"""

    def test_mutation(self):
        """code after mutation should still be valid read code"""
        code = readcode.generate(5)

        mutated = genetic_operations.mutate(code)

        self.assertTrue(readcode.is_valid(mutated))

    def test_crossover(self):
        """should return two trees, both should be valid"""
        code_a = [(2,), (1,), (0,), (2,), (1,), (0,), (0,)]
        code_b = [(3,), (2,), (1,), (0,), (0,), (0,), (1,), (2,), (0,), (0,)]

        print('pred', code_a, code_b)

        desc_a, desc_b = genetic_operations.crossover(code_a, code_b)

        print('po  ', desc_a, desc_b)

        self.assertTrue(readcode.is_valid(desc_a))
        self.assertTrue(readcode.is_valid(desc_b))


if __name__ == '__main__':
    unittest.main()
    