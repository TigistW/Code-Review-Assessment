# snippet - 1
# Calculates area of a circle
import math
def calculateArea(radius):
    return math.pi * (radius ** 2)


# Calculates the quotient of two numbers
def divide_numbers(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return
    return a / b

# snippets-2

# validates an iterable whether it is a valid parenthesis sequence or not
def is_valid_parenthesis(givenStr):
    # define a dictionary that defines the valid parenthesis elements and answer space
    hashmap = {
        '(': ')',
          "{": "}",
         '[': ']'
    }
    stack = []
    
    '''
    Looping through the given iterable and whenever finding a closing parenthesis 
    we will check if its opening parenthesis matches the previous parenthesis and it matches as 
    defined in the hashmap.
    
    '''
    for elem in givenStr:
        if elem in hashmap.keys(): stack.append(elem)
        else:
            if len(stack) == 0:
                return False
            punc = stack.pop()
            if hashmap[punc] != elem:
                return False
    if len(stack) != 0:
        return False
    return True
