# Getting Started --------------------------------------
a = 5
b = 3
name, age = 'Natasha', 25

print(my_var:='Hello World!') #Walrus Operator
print('Alice' * 5) #AliceAliceAliceAliceAlice 

# Checking data types --------------------------------------

print(type(True))                # Boolean
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List []
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set {}
print(type((9.8, 3.14, 2.7)))    # Tuple ()

print(type(zip([1,2],[3,4])))    # Set with zip() used
# zip() - an iterator of tuples where the each item in each passed iterator is paired respectively together
# O/P :((1,3),(2,4))
# x = input("Enter no. : ")

# Operators where a = 5, b = 3 --------------------------------------
print("Integer/Floor division : ", a//b)
print("2's square : ", b**b)
print("101 AND 011 : ",a & b)
print("101 OR 011 : ",a | b)
print("101 XOR 011 : ",a^b)
print("Right Shifting 101 with 2 places : ",a>>2) # 101. ->      1.01 -> 1
print("Left Shifting 101 with 2 places : ",a<<2)  # 101. ->  10100.   -> 10100 == 20

'''
    IN BUILT FUNCTIONS - multiline comment
    mathematical operations (abs(), max(), min()), 
    type conversions (int(), str(), list()), 
    input/output operations (input(), print()), 
    sequence operations (len(), sorted(), enumerate() - iterate 
    over a sequence while keeping track of the index of each item), 
    string operations (str.upper(), str.lower(), str.replace()), 
    list operations (list.append(), list.pop(), list.sort()), 
    dictionary operations (dict.keys() - returns all keys, dict.values()
    - returns all values, dict.items() - returns all key-value pairs), 
    file operations (open(), read(), write()), 
    error handling (try, except, assert() - . It checks if 
    a given condition is true, and if not, it raises an AssertionError ), 
'''
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

assert fruits[0] == 'apple', "fruits[0] should be 'apple'"
print('Assertion passed.')


# STRINGS --------------------------------------

print('a' + 'b')
''' 
    \n: new line
    \t: Tab means(8 spaces)
    \\: Back slash
    \': Single quote (')
    \": Double quote (")
'''
print("a\tb")

# Formatting strings
old_formatted_str = 'I am %s of age %f' %(name, age)
print(old_formatted_str)
new_formatted_str = 'I am {} of age {}'.format(name, age)
print(new_formatted_str)
interpolated_formatted_str = f'I am {name} of age {age}'
print(interpolated_formatted_str)

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

greeting = 'Hello, World!'
print(greeting[::-2]) # !lo olH - alternate characters

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# String Methods

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(1)) # 'thirty days of python'

challenge = '30DaysPython'
print(challenge.isalnum()) # True - Checks alphanumeric character
# isdecimal(), isalpha(), isidentifier() - valid variable name,
# isnumeric(), isDigit(), islower(), isupper() are more..

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
print(challenge.capitalize()) # 'Thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 19)) # 2, 
print(challenge.count('th')) # 2`
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print(challenge.find('y'))  # 5 - first occurence
print(challenge.find('th')) # 0
print(challenge.rfind('y'))  # 16 - last occurence
print(challenge.rfind('th')) # 17
print(challenge.index('da'))  # 7 - lowest index of substring
print(challenge.rindex('da'))  # 8 - highest index of substring
# print(challenge.index('da', 9)) # error
# print(challenge.rindex('da',9)) # error
print(', '.join(fruits)) # Returns a concatenated string
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
print(challenge.split(', ')) # ['thirty days of python']
print(challenge.title()) # Thirty Days Of Python
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
print(challenge.startswith('thirty')) # True

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# Displaying the table --------------------------------------

def power(x, n):
    return x ** n

for i in range(1, 6):
    row = f"{i} "
    for j in range(4):
        row += f" {power(i, j)} "
    print(row)

# 1  1  1  1  1
# 2  1  2  4  8
# 3  1  3  9  27
# 4  1  4  16  64
# 5  1  5  25  125
    
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')
print('cats', 'dogs', 'mice', sep=',')

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

if 3>1:
    print(3)
else:
    print(1)

def typeIs(n): 
    print(type(n))

typeIs(23)

y = 0.1*3
if(y != 0.3):
    print(y)
else:
    print("peace")

for i in range(1,10,2): #1-10 leaving 2
    print(i)


from decimal import *
  
getcontext().prec = 6

y = Decimal("0.1")*3
if(y != Decimal("0.3")):
    print("missile")
else:
    print("peace")

# anonymous 
    

x = lambda a : a+10
print(x(5))

# list  - ordered collection

l1 = [1,2,3,4,3]
l2 = l1.append([5])
# print(list1[-1] ) # add length
# list1.split(2,3)
# print(l1 * 3) # [1, 2, 3, 4, 3, 1, 2, 3, 4, 3, 1, 2, 3, 4, 3]
print(l1)

#STRING
s = "The dfwsges"
print(s[0:3])

# Function with default paramerter : 
def twoZa(n, m = 2):
    return m*n
print(twoZa(3))

# Arbitrary Number of Arguments
def show(*a):
    for i in a:
        print(i)
show(12,34,5,677)

# Function as a Parameter of Another Function
def square(n):
    return n*n
def cube(n):
    return n*n*n

def calculate(fun, par):
    return fun(par)
print(calculate(square, 3))
print(calculate(cube,2))












