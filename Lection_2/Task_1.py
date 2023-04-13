'''Counting the Number of Input Elements'''

amount = 3
print(f'Please Enter {amount} sentence')

elements = []

while amount != 0:
    sentence = int(input('Enter count words in sentence: '))
    for _ in range(sentence):   
        elements.append(input('Enter word: '))
    amount -= 1
print(f'Amount words = {len(elements)}')
