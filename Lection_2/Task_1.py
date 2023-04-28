'''Counting element'''

elements = input('Enter elements through space: ').split(' ')
element = input('Write an element to count: ')

if element in elements:
    print('Chosen element "{}": where {} it count repetition!'.format(element, elements.count(element)))
else:
    print(f'Chosen element "{element}" not found')