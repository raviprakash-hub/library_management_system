from Book import Book

class Catalog:

    def searchByName(self, name= "an"):
        for book in Book.get_all_books():
            if book.name == name:
                print("the {} written by {}".format(book.name,book.author))
                return book
        else:
            print("no book found")
            return None

    def searchByAuthor(self, author):
        for book in Book.get_all_books():
            if book.author == author:
                print("Author {1} has written the book {}".format(book.name,book.author))
                return book
        else:
            print("no book found")
            return None

