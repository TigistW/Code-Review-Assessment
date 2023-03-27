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
def is_valid_parenthesis(s):
    # define a dictionary that defines the valid parenthesis elements and answer space
    dc = {
        '(': ')',
          "{": "}",
         '[': ']'
    }
    stack = []
    
    for i in s:
        if i in dc.keys(): stack.append(i)
        else:
            if len(stack) == 0:
                return False
            
            op = stack.pop()
            if dc[op] != i:
                return False
    if len(stack) != 0:
        return False
    return True
