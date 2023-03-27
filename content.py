# snippet - 1
def calculateArea(radius):
    return 3.14 * radius ** 2


def divide_numbers(a, b):
    return a / b

# snippet - 2


def is_valid_parenthesis(s):
    dc = {
        '(': ')',
        "{": "}",
        '[': ']'

    }
    stack = []
    for i in s:
        if i in dc.keys():
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            op = stack.pop()
            if dc[op] != i:
                return False
    if len(stack) != 0:
        return False

    return True
