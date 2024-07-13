''' 
# Methods in re Module
    re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
    re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
    re.findall: Returns a list containing all matches
    re.split: Takes a string, splits it at the match points, returns a list
    re.sub: Replaces one or many matches within a string

SYNTAX:
    re.match(string_or_pattern, string_to_look, re.I)
    # re.I is case ignore

'''

import re

string = 'Work? I work at NucleusTeq'
string_to_look_for = 'Work'

ans = re.match(string_to_look_for, string, re.I)
ans = re.findall(string_to_look_for, string, re.I)
ans = re.findall('Work|work', string)
ans = re.findall('[Ww]ork', string)
ans = re.search(string_to_look_for, string, re.I)
ans = re.sub('at', 'with', string, re.I)
ans = re.split(' ', string)
print(ans)

''' 
# Writing RegEx Patterns

    r'x'    regex pattern variable = x
    [x-y]   range/set of characters x to y
    \d      digit
    \D      non digits
    r'^x'   starts with x
    $x      ends with x
    [^x]    not x
    .       any one character (except \n)
    [x]*    x zero or more times
    [x]+    x one or more times
    [x]?    x zero or one time

'''