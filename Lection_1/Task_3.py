# Calculate

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

operation = input('Enter operation: ')

match operation:
    case '+':
        print(f'Result: {number1 + number2}')
    case '-':
        print(f'Result: {number1 - number2}')
    case '*':
        print(f'Result: {number1 * number2}')
    case '/':
        print(f'Result: {number1 / number2}')
    case '**':  # Find out the number in the degree
        print(f'Result: {number1 ** number2}')
    case '//':  # Find the whole part
        print(f'Result: {number1 // number2}')
    case '%':  # Find remainder of a number
        print(f'Result: {number1 % number2}')
    case _:
        print('Wrong Enter!')