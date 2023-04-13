# Sets

amount = int(input('How many set elements would you like enter: '))
general_list = []

for index_set in range(1, amount + 1):
    general_list.append(input('Enter elements by spaces: ').split())
    print(f'{index_set} set elements added')

#No unique from lists

NotUniqueElements = []

for data_set in general_list:
    for not_unique in data_set:
        if data_set.count(not_unique) > 1:
            NotUniqueElements.append(not_unique)

print('----------------------------')

print(f'No unique elements from lists {NotUniqueElements}')

print('----------------------------')

print(f'Final result UNIQUE elements from 3 No unique lists: {set(NotUniqueElements)}')
