# Calculate

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

operation = input('Enter operation: ')

match operation:
    case '+':
        value = number1 + number2
    case '-':
        value = number1 - number2
    case '*':
        value = number1 * number2
    case '/':
        value = number1 / number2
    case '**':  # Find out the number in the degree
        value = number1 ** number2
    case '//':  # Find the whole part
        value = number1 // number2
    case '%':  # Find remainder of a number
        value = number1 % number2
    case _:
        value = 'Wrong Enter'

print(f'Result: {value}')
