from math import log
from random import randint
from random import choice

from utils.dictionary import reverse
from utils.dictionary import convert_to_args_n

class Environment():
    def __init__(self, symbols):
        self.symbols_inv = reverse(convert_to_args_n(symbols))
        self.symbols = symbols


class BasicEnvironment(Environment):

    def __init__(self):

        def random_int():
            while True:
                yield str(randint(-5, 5))

        random_int_generator = random_int()

        def random_var():
            while True:
                yield choice(['x', 'y']) 

        random_var_generator = random_var()

        symbols = {
            '_sum': lambda x, y: x + y,
            '_diff': lambda x, y: x - y,
            '_log': lambda x: log(x),
            '_int': lambda: next(random_int_generator),
            '_var': lambda: next(random_var_generator)
        }

        super().__init__(symbols)
