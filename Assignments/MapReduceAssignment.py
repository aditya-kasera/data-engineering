def split(line):
    words = line.split()
    return words

def mapper(line):
    dict = {}
    for word in split(line):
        if word in dict:
            dict[f'{word}'] += 1
        else:
            dict[f'{word}'] = 1
    return dict

def reducer(mapped_dict_list):
    reduced_dict = {}
    for dict in mapped_dict_list:
        for key, value in dict.items():
            if key in reduced_dict:
                reduced_dict[key] += value
            else:
                reduced_dict[key] = value
    return reduced_dict


with open(r'Assignments\MapReduceFile.txt', 'r') as file:
    
    lines = file.read().splitlines()

    mapped_dict_list = []
    for line in lines:
        mapped_dict_list.append(mapper(line)) # map all the lines

    reduced_dict = reducer(mapped_dict_list) # reduce the list of all mapped dictionaries

    print(reduced_dict) #final reduded dictionary
    


'''
OUTPUT:

PS D:\PROGRAMMING\Python> python -u "d:\PROGRAMMING\Python\Assignments\MapReduceAssignment.py"
{'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 3, 'lazy': 1, 'dog.': 1, 'How': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 3, 'woodchuck': 2, 'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1, 'Peter': 1, 'Piper': 1, 'picked': 1, 'peck': 1, 'Of': 1, 'pickled': 1, 'peppers.': 1, 'She': 1, 'sells': 1, 'seashells': 1, 'by': 1, 'keashore.': 1, 'I': 1, 'scream,': 2, 'you': 1, 'we': 1, 'all': 1, 'scream': 1, 'for': 1, 'ice': 1, 'cream.': 1, 'To': 1, 'be': 1, 'or': 1, 'not': 1, 'to': 1, 'be,': 1, 'that': 2, 'is': 1, 'question.': 1, "All's": 1, 'well': 1, 'ends': 1, 'well.': 1}
PS D:\PROGRAMMING\Python> 
'''


