from User import User
from Book import Book
from Library import Library
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id, emp_id,library):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        self.library = library
        
    def add_book(self, name, author, publish_date, pages):
        self.book = Book(name, author, publish_date, pages)
        print ("enter the isbn and rack number")
        isbn = input()
        rack = int(input())
        self.library.add_book_to_rack(self.book,rack,isbn)
    
    def delete_book(self,isbn):
        self.library.remove_book_from_rack(isbn)

    def display_all_book(self):
        self.library.display_all_data()

    def search_book(self):
        print("how you want to search")
        print("1)name\n2)author\n3)isbn\n4)exit")
        number = int(input("enter your choice: "))
        if number == 1:
            name = input("enter name  :  ")
            self.library.search_book_by_name(name)
        elif number == 2:
            name = input("enter author name  : ")
            self.library.search_book_by_author(name)
        elif number == 3:
            name = int(input("enter isbn :  "))
            print("Book present in",self.library.search_book_by_isbn(name)+1)
        else:
            return