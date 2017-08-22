"""
Module containing functions for genetic operations
"""
from inspect import signature as sg
from random import choice

from tree.tree import Tree
from tree.node import Node
from utils.lists import add

def point_mutate(tree):
    # choose random node
    node_id = choice(tree.node_ids)
    
    # determine whether it is leaf or node
    is_leaf = len(tree.hash_map[node_id]) == 0

    if is_leaf:
        # pick random terminal
        new_symbol = choice(tree.environment.terminals)
    else:
        # check how many arguments it has to take
        old_symbol = tree.nodes[node_id]
        n_args = len(sg(tree.environment.nonterminals[old_symbol.value]).parameters)
        # and pick random nonterminal
        new_symbol = choice(tree.environment.reversed_n_args[n_args])

    mutated_tree = tree.copy()

    mutated_tree.nodes.update({node_id: Node(node_id, new_symbol)})

    return mutated_tree

def crossover(father, mother):
    # choose random crossover points from father and mother
    father_crosspoint = choice(father.node_ids)
    mother_crosspoint = choice(mother.node_ids)

    f_subtree_edges, f_subtree_values = father.subtree(father_crosspoint)
    m_subtree_edges, m_subtree_values = mother.subtree(mother_crosspoint)

    largest_father_id = father.node_ids[-1]
    largest_mother_id = mother.node_ids[-1]

    # edges
    father_without = set(father.edges) - set(f_subtree_edges)
    mother_without = set(mother.edges) - set(m_subtree_edges)
    
    f_subtree_edges = [(x+largest_father_id , y + largest_father_id) for x, y in f_subtree_edges]
    m_subtree_edges = [(x+largest_mother_id , y + largest_mother_id) for x, y in m_subtree_edges]


    child_a_edges = father_without.union(set(m_subtree_edges))
    child_b_edges = mother_without.union(set(f_subtree_edges))

    child_a_edges = [(p,c+largest_father_id) if c == father_crosspoint
                        else (p,c) for p, c in child_a_edges]
    child_b_edges = [(p,c+largest_mother_id) if c == father_crosspoint
                        else (p,c) for p, c in child_b_edges]

    # values    
    f_subtree_values_set = set(f_subtree_values.items())
    m_subtree_values_set = set(m_subtree_values.items())
    
    f_values_without = set(father.values.items()) - set(f_subtree_values_set)
    m_values_without = set(mother.values.items()) - set(m_subtree_values_set)

    child_b_values = {k+largest_father_id:v for k,v in f_subtree_values_set}
    child_b_values = {**child_b_values, **dict(m_values_without)}
    

    child_a_values = {k+largest_mother_id:v for k,v in m_subtree_values_set}
    child_a_values = {**child_a_values, **dict(f_values_without)}

    print(child_a_values, child_a_edges)

    child_a = Tree(child_a_edges, father.environment, child_a_values)
    child_b = Tree(child_b_edges, mother.environment, child_b_values)



    child_a.remap()
    child_b.remap()

    return child_a, child_b








