from copy import deepcopy

class Individual():
    """
    Wraps the expression tree and stores its fitness
    """

    def __init__(self, trees, variables):
        self.trees = trees
        self.fitness = None
        self.vars = variables

    def eval_on_row(self, row, cost_function, symbols):
        inputs = {k:v for k,v in zip(self.vars, row)}
        outputs = []
        for tree in self.trees:
            outputs.append(tree({**symbols, **inputs}))
        return outputs

    def eval_on_data(self, data, cost_function, symbols):
        """
        Apply the transformation by trees on each line of data
        and calls the cost_function callback with results
        """
        y_test = []

        for row in data:
            outputs = self.eval_on_row(row, cost_function, symbols)
            y_test.append(outputs)

        self.fitness = cost_function(y_test)

    def copy(self):
        return deepcopy(self)

    def __str__(self):
        return '\n'.join([str(tree) for tree in self.trees])
