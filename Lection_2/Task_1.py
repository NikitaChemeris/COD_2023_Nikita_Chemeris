'''Counting the Number of Input Elements'''

N = 3
print(f'Please Enter {N} sentence')

elements = []

while N != 0:
    sentence = int(input('Enter count words in sentence: '))
    for i in range(sentence):
        elements.append(input('Enter word: '))
    N -= 1
print(f'Amount words = {len(elements)}')