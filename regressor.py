"""
Trieda vykonavajuca symbolicku regresiu
"""

class GpRegression(bobject):

    def __init__(self):
        self.mutation_p = 0.1
        self.crossover_p = 0.9

    def fit(self, X, y, fitness):
        population = [(self._generate_expresion(), None) for i in range(0,500)]
        population = self._eval_fitness(population)

    def _eval_fitness(self, population):
        evalued = []
        for individual in population:
            try:
                X = candidate_solution_func(individual[0], data[:,0])
            except (ValueError, ZeroDivisionError) as ve:
                print(ve)
                continue
            
            error = mse(data[:,1], X)
            #print(readcode.parse(individual[0]), error)
            evalued.append((individual[0], error))
        evalued.sort(key=lambda x: x[1])
        return [x for x in evalued if float('-inf') < float(x[1]) < float('inf')]

    def _generate_expresion(self):
        tree = readcode.generate(3)
        tree_with_symbols = symbols.assign_symbols(tree)
        return tree_with_symbols
    