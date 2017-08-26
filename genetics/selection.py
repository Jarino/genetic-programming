from random import sample

def tournament_selection(population, tournament_size):
    """
    population - list of Individual
    """

    picked = sample(population, tournament_size)

    picked.sort(key=lambda x: x.fitness)

    return picked[0]
