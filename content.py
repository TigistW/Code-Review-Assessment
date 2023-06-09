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
        if elem in hashmap.keys():
            stack.append(elem)
        else:
            if len(stack) == 0:
                return False
            punc = stack.pop()
            if hashmap[punc] != elem:
                return False
    if len(stack) != 0:
        return False
    return True



# snippet - 3
# returns the square of a number
def get_square(number):
    return number ** 2

# returns the cube of each value in the array
def get_cubes(numbers):
    cubes = []
    for number in numbers:
        cubes.append(number ** 3)
    return cubes


my_numbers = [1, 2, 3, 4, 5]
squares = []
for number in my_numbers:
    squares.append(get_square(number))

# holds the cube values of my_numbers array
cubes = get_cubes(my_numbers)

# snippets-4

#accept two numbers and return their multiplicaion
def multiplication(num1, num2):
    return num1 *  num2

# increase count variable while function called

count = 0
def increment_count():
    global count
    count += 1

increment_count()
print(count)


