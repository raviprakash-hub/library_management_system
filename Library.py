from Rack import Rack
from BookData import BookData

class Library:
    book_count = 0
    books = []
    rack_dict = {}

    def __init__(self,rack_count,rack_size):
        self.book = None
        self.isbn = 0
        for i in range(rack_count):
            Library.rack_dict.setdefault(i+1,Rack(rack_size))

    def add_book_to_rack(self,book,rack_no,isbn):
        rack = Library.rack_dict.get(rack_no)
        if rack.size > rack.item_count:
            rack.add_book_to_rack(book,isbn)
            return True
        else:
            rack = input("rack is full please enter different rack or press q to quit")
            if rack == "q":
                return
            else:
                return self.add_book_to_rack(book,int(rack_no),isbn)
        
    def delete_book_from_rack(self,rack_no,isbn):
        rack = Library.rack_dict[rack_no]
        rack.delete_book_in_rack(isbn)
        Library.rack_dict[rack_no] = rack

    def display_all_data(self):
        print ("Rack number \t data \t isbn")
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            rack.display_data_in_rack(i+1)

    def search_book_by_name(self,name):
        flag = False
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            for book_data in rack.rack_table:
                if book_data.book.name == name:
                    print("Book {} is prsesnt in rack no {}".format(name,i+1))
                    flag = True
        else:
            if not flag:
                print("No books found")

    def search_book_by_author(self,name):
        flag = False
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict.get(i+1)
            for book_data in rack.rack_table:
                if book_data.book.author == name:
                    print("Book {} written by {} is prsesnt in rack no {}".format(book_data.book.name,name,i+1))
                    flag = True
        else:
            if not flag:
                print("No books found for this author")
            
    def search_book_by_isbn(self,isbn):
        for i in range(len(Library.rack_dict)):
            rack = Library.rack_dict[i+1]
            for book_data in rack.rack_table:
                if book_data.isbn == isbn:
                    return i
                    
        else:
            return None

    def remove_book_from_rack(self,isbn):
        rack_number = self.search_book_by_isbn(isbn)+1
        rack = None
        if rack_number:
            rack = Library.rack_dict[rack_number]
        if rack:
            rack.delete_book_in_rack(isbn)
        else:
            print("err")
        

    def issued_book(self,isbn):
        rack_number = self.search_book_by_isbn(isbn)
        rack = Library.rack_dict[rack_number+1]
        book = rack.issue_book(isbn)
        self.remove_book_from_rack(isbn)
        return book

    def accept_return_book(self,book_data,rack_no):
        rack = Library.rack_dict[rack_no+1]
        if rack.size > rack.item_count:
            rack.add_return_book_to_rack(book_data)
            return True
        else:
            return False