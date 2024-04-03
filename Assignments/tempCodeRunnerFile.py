mapped_dict_list):
    reduced_dict = {}
    for dict in mapped_dict_list:
        for key, value in dict.items():
            if key in reduced_dict:
                reduced_dict[key] += value
            else:
                reduced_dict[key] = value
    return r