# Update card file

def add(CardFile, BookId):
    description = {
        'Name': input('Name book: '),
        'Author': input('Author book: '),
        'Count pages': int(input('Count pages book: ')),
        'Genre': input('Genre book: '),
        'Binding': input('Binding (solid/soft) book: ')
    }

    CardFile[BookId] = description
    print('Book id {} and name book "{}" added'.format(BookId, description['Name']))
    return CardFile, BookId + 1


def delete(CardFile, delete_id):
    if delete_id in CardFile:
        print(f'Book id {delete_id} and name book "{CardFile[delete_id]["Name"]}" deleted')
        del CardFile[delete_id]
    else:
        print(f'Book Id {delete_id} not found')
    return CardFile


def edit(CardFile, edit_id):
    if edit_id in CardFile:
        category = input("""What do you want to edit? Select and write in Enter:
1.Name
2.Author
3.Count pages
4.Genre
5.Binding
Please, Enter: """)
        if category in CardFile[edit_id]:
            update = input('Edit on: ')
            CardFile[edit_id][category] = update
            print('The {} book id {} replaced by {}'.format(category, edit_id, update))
        else:
            print(f'Invalid category: {category}')
    else:
        print(f'Book Id {edit_id} not found')
    return CardFile


def found():
    print(f'Your id and name book : {[(key, value["Name"]) for key, value in CardFile.items()]}')
    info = input('Would you like to look up info about book? (Yes/No): ')
    if info == 'Yes':
        input_id = int(input('Please enter id book: '))
        print(CardFile.get(input_id, f'Book Id {input_id} not found'))


CardFile = {}
BookId = 0
function = None

while function != 'Close':
    function = input('''Select and Write a function for a book:
- Add book
- Delete book
- Edit book
- Found book
- Close
Enter: ''')

    match function:
        case 'Add book':
            CardFile, BookId = add(CardFile, BookId)
        case 'Delete book':
            delete_id = (int(input('Write book id which you want delete: ')))
            CardFile = delete(CardFile, delete_id)
        case 'Edit book':
            edit_id = (int(input('Write Id book and will edit this: ')))
            CardFile = edit(CardFile, edit_id)
        case 'Found book':
            found()
        case 'Close':
            print('See you around :)')
        case _:
            print('Wrong Enter!')

    print('-' * 35)
