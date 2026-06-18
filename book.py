books = [
    "Python Programming",
    "Data Structures",
    "Database Management",
    "Computer Networks",
    "Operating Systems"
]                                                                              

search_book = input("Enter the book name: ")

found = False


for i in range(len(books)):
    if books[i].lower() == search_book.lower():
        print("Book found at shelf position", i + 1)
        found = True
        break

if not found:
    print("Book not available in the library")