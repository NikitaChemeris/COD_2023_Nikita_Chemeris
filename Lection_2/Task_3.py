# 3 sets

set1 = set(input('Enter elements for the first set, separated spaces: ').split())
set2 = set(input('Now for the second set: ').split())
set3 = set(input('And finally for the third set: ').split())

print(f'Unique elements from 3 sets: {set1 ^ set2 ^ set3}')
