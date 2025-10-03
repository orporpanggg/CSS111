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

#ทดสอบ function add_book
print("book 0")
add_book(books, "111", "Python 101", "Alice", 5)

print("book 1")
add_book(books, "111", "Python 101", "Alice", 5)

print("book 2")
add_book(books, "222", "Learn C++", "Bob", 3)
    
#ทดสอบ function search_books
add_book(books, "001", "python programming", "alice johnson", 5)
add_book(books, "002", "learn django", "bob smith", 3)
add_book(books, "003", "data science basics", "charlie brown", 7)

print("keyword: 'python'")
search_books(books, "python")

print("\nkeyword: 'bob'")
search_books(books, "bob")

print("\nkeyword: 'science'")
search_books(books, "science")

print("\nkeyword: 'javascript'")
search_books(books, "javascript")

#ทดสอบ function display_books
display_books(books)