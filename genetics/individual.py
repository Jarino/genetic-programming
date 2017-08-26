from copy import deepcopy

class Individual():
    """
    Wraps the expression tree and stores its fitness
    """

    def __init__(self, trees, variables):
        self.trees = trees
        self.fitness = None
        self.vars = variables

    def eval_on_data(self, data, cost_function, symbols):
        y_test = []

        for row in data:
            inputs = {k:v for k,v in zip(self.vars, row)}
            outputs = []
            for tree in self.trees:
                outputs.append(tree({**symbols, **inputs}))
            y_test.append(outputs)

        self.fitness = cost_function(y_test)

    def copy(self):
        return deepcopy(self)