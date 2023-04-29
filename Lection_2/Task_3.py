# Sets

general_list_sets = []
NonUniqueElements = []

for index_set in range(1, 4):
    sets = set(input(f'Enter {index_set} set elements through a space: ').split(' '))
    general_list_sets.append(sets)
print('Sets done!\n')

for element in general_list_sets[0]:  # We don't need check other lists through for
    if element in general_list_sets[1] and element in general_list_sets[2]:
        NonUniqueElements.append(element)

print(f'Non unique elements: {NonUniqueElements}')
