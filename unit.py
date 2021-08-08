import sys
from Book import Book
from Catalog import Catalog
from Librarian import Librarian
from Member import Member
from Library import Library


b1 = Book("java","abcd","12",47)
b2 = Book("python","pqrs","13",48)
b3 = Book("crg","mnop","14",49)
print(Book.get_all_books())
1
library = Library(5,5)
library.add_book_to_rack(b1,1,1)
library.add_book_to_rack(b2,2,1)
library.add_book_to_rack(b3,1,2)

member1 = Member("CRG","Banglore",22,889128319,123123,library)
member2 = Member("vinay","mumbai",23,8899788789,123124,library)
member3 = Member("ibad","delhi",21,889128318,123123,library)
