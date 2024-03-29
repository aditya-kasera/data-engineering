def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def is_prime(n):

    # EXCEPTION HANDLING
    if type(n) != int:
        raise TypeError('Number is of invalid type.')
    if(n < 0):
        raise ValueError('Number should be a non-negative integer.')
    
    #LOGIC
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# MANUAL TESTING - inefficient
# >>> from Unit import add
# >>> add(2,4)
# 6
# >>> assert add(10,5) == True                              
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError

#  return value from the function is different than the expected Boolean value, an AssertionError is raised.