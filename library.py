books = []
def add_book(books, ISBN, name, author, book_count):
    for b in books:
        if b['ISBN'] == ISBN :
            print("failed to add - already had this book")
            return False
    new_book = {
        "name": name,
        "author": author,
        "ISBN": ISBN,
        "book_count": book_count
    }
    books.append(new_book)
    print("book added successfully")
    return True

def search_books(books, keyword):
    found = False
    for b in books:
        if keyword in b['name'] or keyword in b['author']:
            print(f"- {b['name']} by {b['author']} (ISBN: {b['ISBN']}, copies: {b['book_count']})")
            found = True
    if not found:
        print("book not found")
        
def display_books(books):
    print("All books in the system:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['name']} by {book['author']} (ISBN: {book['ISBN']}, copies: {book['book_count']})")

add_book (books,' 001''Python Crash Course', 'Eric Matthes', 3)
add_book (books,' 002''Clean Code', 'Robert Martin', 2)
add_book (books,' 003''The Pragmatic Programmer','Hunt & Thomas', 2)
add_book (books,' 004''Design Patterns', 'Gang of Four', 1)
add_book (books,' 005''Introduction to Algorithms', 'Cormen et al.', 2)
add_book (books,' 006''Code Complete', 'Steve McConnell', 3)
add_book (books,' 007", 'Refactoring', 'Martin Fowler', 2)
