# Card file

CardFile = {}
function = None
BookId = 1

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

            CardFile[BookId] = {'Name': name,
                                'Author': author,
                                'Count pages': pages,
                                'Genre': genre,
                                'Binding': binding}

            print(f'Id {BookId} and book "{name}" added')
            BookId += 1
            print('------------------')
        case 'Remove book':
            DeleteBook = int(input('Write id book, if you want delete it: '))
            del CardFile[DeleteBook]
            print(f'Book id "{DeleteBook}" successfully removed')
            print('------------------')
        case 'Edit book':
            id = int(input('Enter id book: '))
            category = input('''What do you want to edit? Select and write in Enter:
- Name
- Author
- Count pages
- Genre
- Binding
Enter: ''')
            CardFile[id][category] = (edit := input('Edit on: '))  # "edit" for format
            print('The {} by book id {} replaced by {}'.format(category, id, edit))
            print('------------------')
        case 'Found book':
            print(f'Your id and name book : {[(key, value["Name"]) for key, value in CardFile.items()]}')

            info = input('Would you like look info about book? Yes or No: ')

            if info == 'Yes':
                book_id = int(input('Please enter id book: '))
                print(CardFile[book_id])
            print('------------------')
        case 'Cancel':
            print('Good bye :)')
        case _:
            print('Wrong Enter!')
