# 3 sets

list1 = list(input('Enter elements for the first list, separated spaces: ').split())
list2 = list(input('Now for the second list: ').split())
list3 = list(input('And finally for the third list: ').split())

#No unique from lists

NonUnique1 = [i for i in list1 if list1.count(i) > 1]
NonUnique2 = [o for o in list2 if list2.count(o) > 1]
NonUnique3 = [y for y in list3 if list3.count(y) > 1]

print('----------------------------')

print('''No unique elements from lists
First list: {}
Second list: {}
Third list: {}'''.format(NonUnique1, NonUnique2, NonUnique3))

print('----------------------------')

NoUnique = set(NonUnique1) ^ set(NonUnique2) ^ set(NonUnique3)
print(f'Final result UNIQUE elements from 3 No unique lists: {NoUnique}')
