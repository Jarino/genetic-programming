"""Modul obsahujuci geneticke operatory mutacie a krizenia dvoch stromov"""

import random
import readcode

def mutate(code):
    """
    Vyberieme si nahodny neterminalny ony a nahradime ho novym
    Neterminalny je ten, ktory je vacsi ako nula
    """
    chosen = random.randint(1, len(code) - 1)

    subtree = readcode.generate(4)

    subtree_len = readcode.subtree_length(code, chosen)

    return code[0:chosen] + subtree + code[chosen + subtree_len:]

def crossover(code_a, code_b):
    """
    operacia krizenia medzi dvoma stromami
    """

    index_a = random.randint(1, len(code_a) - 1)
    index_b = random.randint(1, len(code_b) - 1)

    subtree_a_len = readcode.subtree_length(code_a, index_a)
    subtree_b_len = readcode.subtree_length(code_b, index_b)

    subtree_a = code_a[index_a:index_a + subtree_a_len]
    subtree_b = code_b[index_b:index_b + subtree_b_len]

    desc_a = code_a[0:index_a] + subtree_b + code_a[index_a + subtree_a_len:]
    desc_b = code_b[0:index_b] + subtree_a + code_b[index_b + subtree_b_len:]

    return desc_a, desc_b
