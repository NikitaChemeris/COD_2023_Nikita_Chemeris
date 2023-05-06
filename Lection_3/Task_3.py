# Update card file

CardFile = {}


def add():
    description = {
        'Name': input('Name book: '),
        'Author': input('Author book: '),
        'Count pages': int(input('Count pages book: ')),
        'Genre': input('Genre book: '),
        'Binding': input('Binding (solid/soft) book: ')
    }

    print('Book id {} and name book "{}" added'.format(BookId, description['Name']))
    return description


def delete(input_id):
    print(f'Book id {input_id} and name book "{CardFile[input_id]["Name"]}" deleted')
    del CardFile[input_id]
    return input_id


def edit(change_BookId):
    category = input("""What do you want to edit? Select and write in Enter:
1.Name
2.Author
3.Count pages
4.Genre
5.Binding
Please, Enter: """)
    update = input('Edit on: ')

    CardFile[change_BookId][category] = update
    print('The {} book id {} replaced by {}'.format(category, change_BookId, update))
    return CardFile


def found():
    print(f'Your id and name book : {[(key, value["Name"]) for key, value in CardFile.items()]}')

    info = input('Would you like look info about book? Yes or No: ')

    if info == 'Yes':
        input_id = int(input('Please enter id book: '))
        print(CardFile[input_id])


BookId, function = 0, None

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
            CardFile[BookId] = add()
            BookId += 1
        case 'Delete book':
            delete(int(input('Write book id which you want delete: ')))
        case 'Edit book':
            edit(int(input('Write Id book and will edit this: ')))
        case 'Found book':
            found()
        case 'Close':
            print('See you around :)')
        case _:
            print('Wrong Enter!')

    print('-' * 35)
