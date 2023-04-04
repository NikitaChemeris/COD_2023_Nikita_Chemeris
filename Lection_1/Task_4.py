'''Quadratic equation'''

print('For quadratic equation we used formula (ax**2 + bx + c = 0), where "**" - degree!')

a = float(input("Enter number 'a': "))
b = float(input("Enter number 'b': "))
c = float(input("Enter number 'c': "))

D = b ** 2 - 4 * a * c  # Discriminant

if a == 0:
    print("'a' can't be zero")
elif D < 0:
    print('No real roots in Discriminant')
else:
    print(f'x1 = {(-b + D ** 0.5) / (2 * a)}')
    print(f'x2 = {(-b - D ** 0.5) / (2 * a)}')
