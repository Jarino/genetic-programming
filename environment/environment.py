from math import log

from utils.dictionary import reverse
from utils.dictionary import convert_to_args_n

class Environment():

    def __init__(self, nonterminals, terminals):
        self.nonterminals = nonterminals
        self.n_args = convert_to_args_n(self.nonterminals)
        self.reversed_n_args = reverse(self.n_args)
        self.terminals = terminals


class BasicEnvironment(Environment):

    def __init__(self):
        nonterminals = {
            '_sum': lambda x, y: x + y,
            '_diff': lambda x, y: x - y,
            '_log': lambda x: log(x)
        }
        terminals = [str(x) for x in range(0,5)]
        terminals.append('x')
        terminals.append('y')
        super().__init__(nonterminals, terminals)
