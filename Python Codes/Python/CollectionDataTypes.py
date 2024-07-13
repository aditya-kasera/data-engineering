# LIST - ordered and modifiable. Allows duplicate members, heterogenous
# TUPLE - ordered and immutable. Allows duplicate members, heterogenous
# SET -  unordered, un-indexed and immutable, but we can add new items to the set. Duplicate members are not allowed.
# DICTIONARY - key-value pair collection - unordered, modifiable and indexed. No duplicate members.

l1 = list()
print(len(l1)) # 0

l2 = []
l2 = [11,22,33,44]
print(l2[0]) # 11
print(l2[1]) # 22
print(l2[2]) # 33
print(l2[3]) # 44
print(l2[-1]) # 44 - last
print(l2[-2]) # 33
print(l2[-3]) # 22
print(l2[-4]) # 11 - first

one, two, three, four = l2;
print(f'{one, two, three, four}') # Unpacking List Items
mid = l2[1:3] # [n,m) - slicing copy of a subset
print(mid)
mid = l2[1:-2]
print(mid)

print(l2[1:]) # from index 1
print(l2[:]) # full

l2_independent = l2[:] # Independent copies, two references
l2_independent.append(55)
print(l2_independent[-1])
print(l2[-1])

l2_ref = l2 # Both refer to 1 reference, changing one affects both
print(l2_ref[-1])
print(l2[-1])

print(22 in l2) # Be careful: the in keyword is also used in the syntax of for loops and list comprehensions

l2.append(55)
print(l2[4] == l2[-1])

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md#inserting-items-into-a-list

l3 = ['a', 0, (2,3)]
print(l3)
print(l3 + l2) # concatenation - creates a new list with new memory reference
print(l3 * 2) # concatenation

l3[2] = True # Lists are mutable
print(l3) # l3 still points to same memory reference when we’re done. 

l3.insert(1, 'b') # at index 1, insert b
print(l3) # ['a', 'b', 0, True]

l3.extend([1,2,3]) # extension makes list long
print(l3) # ['a', 'b', 0, True, 1, 2, 3]
l3.append(['x','y','z']) # appending adds 1 more index to list
print(l3) # ['a', 'b', 0, True, 1, 2, 3,['x','y','z']]

# Operations on lists only :
print(l3.index('b'))  # index of 1st occurrence - 
print(l3.count('b'))  # number of occurrences - 
l3.remove('b') # remove 1st  -
print(l3)
l3.reverse()    # reverse the list *in place*
print(l3)

l2.sort()  # *,None, True
print(l2)# sort the list *in place* - list itself is modified
# l3.sort(some_function)  # for user defined comparision
# print(l3)

##################### SET ####################

s1 = {1,2,3}
print(1 in s1) # True
s1.add(4)
s1.update([5,6,7]) # {1, 2, 3, 4, 5, 6, 7}
s1.pop

removed_item = s1.pop()

print(s1)
s2 = set(l2)

u = s1.union(s2)
n = s1.intersection(s2)
print(n.issubset(u)) # True
print(u.issuperset(n)) # True
diff = s2.difference(s1)
print(diff)
s2.clear()
del s2


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
st2.isdisjoint(st1) # False -  they have common elements


##################### Dictionary ####################

d1 = {}
person = {
    'first_name':'Aditya',
    'last_name':'Kasera',
    'age':22,
    'country':'Indore',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'JNBH',
        'zipcode':'452001'
        }
    }
print(len(person)) # 4)) # 4
person['course'] = 'BCA' # Adding Items to a Dictionary
person['course'] = 'MCA' # modify
print('course' in person) # True
print(person['course']) # value of course
person.pop('course') #  removes the item with the specified key name
del person['age'] # same as pop()
person.popitem() # removes the last item
print(person)
person_copy = person.copy() #Copy a Dictionary

# Changing Dictionary to a List of Items/Tuples
person_list = person.items()
print(person_list)
keys_list = person.keys() #Getting Dictionary Keys as a List
values_list = person.values() #Getting Dictionary Values as a List
erson.clear() #Clearing a Dictionary
del person #Deleting  a Dictionary


