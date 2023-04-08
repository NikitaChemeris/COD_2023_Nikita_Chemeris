# Update card file

def add():
    global CardFile

    CardFile[BookId] = {
        'Name': input('Name book: '),
        'Author': input('Author book: '),
        'Count pages': int(input('Count pages book: ')),
        'Genre': input('Genre book: '),
        'Binding': input('Binding (solid/soft) book: ')
    }

    return 'Book id {} and name book "{}" added'.format(BookId, CardFile[BookId]['Name'])


def remove(input_id):
    global CardFile

    del CardFile[input_id]

    return f'Book id {input_id} deleted'


def edit(input_id):
    global CardFile

    category = input("""What do you want to edit? Select and write in Enter:
1.Name
2.Author
3.Count pages
4.Genre
5.Binding
Please, Enter: """)

    CardFile[input_id][category] = (edit := input('Edit on: '))

    return 'The {} book id {} replaced by {}'.format(category, input_id, edit)


def found():
    print(f'Your id and name book : {[(key, value["Name"]) for key, value in CardFile.items()]}')

    info = input('Would you like look info about book? Yes or No: ')

    if info == 'Yes':
        input_id = int(input('Please enter id book: '))
        return CardFile[input_id]
    else:
        return ''


CardFile = {}
BookId, function = 0, None
spaces = '-' * 35

while function != 'Close':
    function = input('''Select and Write a function for a book:
- Add book
- Remove book
- Edit book
- Found book
- Close
Enter: ''')

    match function:
        case 'Add book':
            complete = add()
            BookId += 1
        case 'Remove book':
            complete = remove(int(input('Write Id book if you want delete it: ')))
        case 'Edit book':
            complete = edit(int(input('Write Id book and will edit this: ')))
        case 'Found book':
            complete = found()
        case 'Close':
            complete = 'See you around :)'
        case _:
            complete = 'Wrong Enter!'

    print('', complete, spaces, sep='\n')
