from inspect import signature as sg

def reverse(dictionary):
    r_dict = {}
    for key, value in dictionary.items():
        if value not in r_dict:
            r_dict[value] = [key]
        else:
            r_dict[value].append(key)
    
    # sort the symbols for deterministic output
    for key, value in r_dict.items():
        r_dict[key].sort()

    return r_dict


def convert_to_args_n(d):
    return {k: len(sg(v).parameters) for k, v in d.items()}