def add_book(library, title, author, year, isbn, availability):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "availability": availability
    }
    library.append(book)
    return library


def list_books(library):
    if len(library) == 0:
        print("Library currently empty")
        return

    for book in library:
        if book['availability'] == True:
            status = "In shelves"
        else:
            status = "Borrowed"

        print(f"'{book['title']}' by {book['author']} in year {book['year']} - Status: {status}")


if __name__ == "__main__":
    Wits_Library = []

    # Adding books
    Wits_Library = add_book(Wits_Library, "Born a Crime", "Trevor Noah", 2016, "9780399588174", True)
    Wits_Library = add_book(Wits_Library, "Analysis", "Tarens Tau", 2021, "9781234567897", False)

    # Listing all books
    list_books(Wits_Library)