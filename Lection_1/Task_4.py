'''Quadratic equation'''

a, b, c = [float(input()) for i in range(3)]
D = b ** 2 - 4 * a * c  # Discriminant

if a == 0:
    print('Error')
elif D < 0:
    print('No real roots')
else:
    print(f'x1 = {(-b + D ** 0.5) / (2 * a)}')
    print(f'x2 = {(-b - D ** 0.5) / (2 * a)}')
