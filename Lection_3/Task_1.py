# Calculate with def

def add(a, b):
    return a + b


def subtrack(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def devision(a, b):
    return a / b


number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
operation = input('Enter operation: ')

match operation:
    case '+':
        save = (add(number_1, number_2))
    case '-':
        save = (subtrack(number_1, number_2))
    case '*':
        save = (multiplication(number_1, number_2))
    case '/':
        save = (devision(number_1, number_2))
    case _:
        save = 'Wrong Enter!'

print(save)
