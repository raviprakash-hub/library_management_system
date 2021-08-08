from User import User
from BookData import BookData

class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id,library):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.library = library
        self.books = []

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
            print("Book present in rack number",self.library.search_book_by_isbn(name)+1)
        else:
            return

    def issue_book(self,isbn):
        if len(self.books) <= 5:
            book = self.library.issued_book(isbn)
            if book:
                data = BookData(book,isbn)
                self.books.append(data)
            else:
                print("no book available")
        else:
            print("only 5 books can be issued please return the taken books")
    
    def return_book(self):
        print("you have {} books to return select how many you want to return  ".format(len(self.books)))
        self.my_books()
        count = int(input("Enter the value: "))
        if count > len(self.books):
            count = int(input("please enter correct value: ")) 
        print("please select book numbers from 1 to {}".format(count))
        number_list = []
        for _ in range(count):
            number_list.append(int(input())-1)
        for book_no in number_list:
            book_data = self.books[book_no]
            for i in range(5):
                if self.library.accept_return_book(book_data,i):
                    self.books.remove(book_data)
                    return

    def my_books(self):
        if len(self.books) != 0:
            print("***BOOKS****")
            for book_data in self.books:
                book = book_data.book
                print("\nBook name {} author {}".format(book.name,book.author))
            print("*********************")
        else:
            print("\n****No BOOKS*****")

    