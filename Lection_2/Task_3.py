# Sets

general_list_sets = []

for index_set in range(1, 4):
    sets = set(input(f'Enter {index_set} set elements through a space: ').split(' '))
    general_list_sets.extend(sets)
print('Sets done!\n')

NonUnique = []

for element in general_list_sets:
    if general_list_sets.count(element) == 3:
        NonUnique.append(element)


print(f'Non unique elements from 3 sets:{set(NonUnique)}')
