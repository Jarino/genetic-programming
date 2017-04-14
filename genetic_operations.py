"""Modul obsahujuci geneticke operatory mutacie a krizenia dvoch stromov"""

import random
import readcode
import symbols

def mutate(code):
    """
    Vyberieme si nahodny neterminalny ony a nahradime ho novym
    Neterminalny je ten, ktory je vacsi ako nula
    """
    chosen = random.randint(0, len(code) - 1)

    subtree = symbols.assign_symbols(readcode.generate(3))

    subtree_len = readcode.subtree_length(code, chosen)

    return code[0:chosen] + subtree + code[chosen + subtree_len:]

def crossover(code_a, code_b):
    """
    operacia krizenia medzi dvoma stromami
    """

    index_a = random.randint(0, len(code_a) - 1)
    index_b = random.randint(0, len(code_b) - 1)

    subtree_a_len = readcode.subtree_length(code_a, index_a)
    subtree_b_len = readcode.subtree_length(code_b, index_b)

    subtree_a = code_a[index_a:index_a + subtree_a_len]
    subtree_b = code_b[index_b:index_b + subtree_b_len]

    desc_a = code_a[0:index_a] + subtree_b + code_a[index_a + subtree_a_len:]
    desc_b = code_b[0:index_b] + subtree_a + code_b[index_b + subtree_b_len:]

    return desc_a, desc_b

def select_individuals(population):
    """
    Nahodne vyberie dve individua do reprodukcneho procesu
    Populacia je v tvare zoznamu ktory obsahuje tuples, pricom prva polozka
    je syntakticky strom a druha polozka je hodnota fitness. Vyber
    prebieha podla "stochastic acceptance" http://www.staff.amu.edu.pl/~lipowski/roulette.html/
    """
    # najdeme maximum
    best_fitness = max(population, key=lambda x: x[1])[1]

    # na reprodukciu potrebujeme dvoch
    selected = []
    for i in range(0,2):
        not_accepted = True
        while not_accepted:
            treshold = random.random()
            pick = random.choice(population)
            if treshold >= pick[1]/best_fitness:
                selected.append(pick)
                not_accepted = False

    return (selected[0], selected[1])

def generate_new_population(population, limit):
    """
    zo starej generacie vygeneruje novu nasledujucim sposobom:
    - vyberu sa dvaja jedincovia na krizenie
    - s istou mierou nahody sa vykona operacia krizenia a mutacie, alebo sa jednoducho
      skopiruju do novej generacie
    - opakujeme kym nova generacia nie je plna
    """
    new_population = []

    while len(new_population) < limit:
        i_a, i_b = select_individuals(population)

        if random.random() > 0.2:
            new_a, new_b = crossover(i_a[0], i_b[0])
            new_a = mutate(new_a)
            new_b = mutate(new_b)
            new_population += [(new_a, None), (new_b, None)]
        else:
            new_population += [i_a, i_b]
    return new_population

# pop = [([(1, 'sqrt'), (2, '/'), (0, 3), (1, 'sqrt'), (1, 'exp'), (1, 'exp'), (0, 3)],
#   5.5331134776050179),
#  ([(2, '*'), (0, 3), (2, '/'), (0, 3), (1, 'exp'), (1, 'exp'), (0, 2)],
#   5.7679269225673204),
#  ([(1, 'exp'), (2, '/'), (0, 1), (2, '+'), (0, 1), (1, 'sqrt'), (0, 2)],
#   171.78237444378817),
#  ([(2, '-'), (0, 'x'), (2, '+'), (0, 3), (2, '+'), (0, 3), (0, 1)],
#   5382.3382476834522),
#  ([(2, '-'), (0, 'x'), (2, '-'), (0, 2), (1, 'exp'), (1, 'exp'), (0, 1)],
#   16944.214447313116),
#  ([(1, 'sqrt'), (1, 'exp'), (2, '+'), (0, 4), (2, '*'), (0, 'x'), (0, 3)],
#   445093.69372813025),
#  ([(2, '*'), (0, 2), (1, 'exp'), (1, 'exp'), (2, '-'), (0, 3), (0, 'x')],
#   1.8119184317944695e+179)]

# generate_new_population(pop, 10)