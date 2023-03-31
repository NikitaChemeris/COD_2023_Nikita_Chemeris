# Card file

CardFile = {}
function = None

while function != 'Cancel':
    function = input('''Select and Write a function for a book:
- Add book
- Remove book
- Edit book
- Found book
- Cancel
Enter: ''')
    match function:
        case 'Add book':
            name = input('Name book: ')
            author = input('Author book: ')
            pages = int(input('Count pages book: '))
            genre = input('Genre book: ')
            binding = input('Binding (solid/soft) book: ')

            CardFile[name] = {'Author': author,
                              'Count pages': pages,
                              'Genre': genre,
                              'Binding': binding}

            print(f'Book "{name}" added')
            print('------------------')
        case 'Remove book':
            DeleteBook = input('Write name book, if you want delete it: ')
            del CardFile[DeleteBook]
            print(f'Book "{DeleteBook}" successfully removed')
            print('------------------')
        case 'Edit book':
            name_book = input('Name book: ')
            category = input('''What do you want to edit? Select and write in Enter:
- Name
- Author
- Count pages
- Genre
- Binding
Enter: ''')
            if category == 'Name':
                CardFile[NewName := input('New name book: ')] = CardFile.pop(name_book)  # Rename key
                print(f'New name book - "{NewName}"')
            else:
                CardFile[name_book][category] = (edit := input('Edit on: '))    # "edit" for format
                print('The {} by book "{}" replaced by {}'.format(category, name_book, edit))
            print('------------------')
        case 'Found book':
            print('Names of your books: ', end='')  # I won't replace words :)
            print(*CardFile.keys(), sep=', ')
            print('------------------')
        case _:
            print('Wrong Enter!')
            print('------------------')