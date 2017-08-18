def reverse(dictionary):
    r_dict = {}
    for key, value in dictionary.items():
        if value not in r_dict:
            r_dict[value] = [key]
        else:
            r_dict[value].append(key)
    return r_dict