from BookData import BookData

class Rack:
    def __init__(self,size):
        self.rack_table = []
        self.size = size
        self.item_count = 0
        
    def add_book_to_rack(self,book,isbn):
        book_data = BookData(book,isbn)
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book added successfully")

    def delete_book_in_rack(self,isbn):
        for book_data in self.rack_table:
            if book_data.isbn == isbn:
                self.rack_table.remove(book_data)
                self.item_count -= 1
                print("deleted successfully")
                break
        else:
            print("cannot find the book")

    def issue_book(self,isbn):
        for book_data in self.rack_table:
            if book_data.isbn == isbn:
                return book_data.book
        else:
            return None

    def display_data_in_rack(self,i):
        print(i,end="")
        if len(self.rack_table) != 0:
            for book_data in self.rack_table:
                print("\t\t",book_data.book.name,"\t",book_data.isbn)
        else:
            print("\t\t NO BOOKS")

    def add_return_book_to_rack(self,book_data):
        self.rack_table.append(book_data)
        self.item_count +=1
        print("book returned successfully")
