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
print("******** WELCOME TO LIBRARY *********")
print("Please choose an option to continue \n1)admin\n2)Member\n3)Exit\n")
loginstate = int(input())
member = None

profile_number = 1
if loginstate == 2:
    print("please choose profile\n 1)CRG 2)vinay 3)ibad")
    profile_number = int(input())
    if profile_number == 1 :
        member = member1
    elif profile_number == 2 :
        member = member2
    elif profile_number == 3:
        member = member3
loggedin = False
while(True):
    
    if loginstate == 1:
        
        
        if(not loggedin):
            print("Enter name and password")
            name = input("Username :")
            password = input("Password :")
            if name == "admin" and password == "admin":
                loggedin = True
                librarian = Librarian(name,"Banglore",25,12345678,12345,library)
                continue
        elif loggedin:
            print("please choose any one option")
            print("1) add Book\n2) Delete Book\n3) Display all books\n4) Search book\n 5) Exit")
            selected = int(input("Enter "))
            if selected == 1:
                print("enter book details")
                name = input("name :")
                author = input("author :")
                publishdate = input("Publish date :")
                pages = int(input("pages :"))
                librarian.add_book(name,author,publishdate,pages)
                continue
            elif selected == 2:
                librarian.display_all_book()
                isbn = int(input("enter isbn number (integer)  "))
                librarian.delete_book(isbn)
                continue
            elif selected == 3:
                librarian.display_all_book()
                continue
            elif selected == 4:
                librarian.search_book()
                continue
            elif selected == 5:
                exit(0)
            else:
                continue
    
    if loginstate == 2:
        
        print("please choose any one option")
        print("1) search Book\n2) issue Book\n3) return books\n4) display all book\n5) See my Books\n6) Exit")
        user_choice = int(input("enter value : "))
        if user_choice not in [1,2,3,4,5]:
            print("please enter valid choice")
            continue
        if user_choice == 1:
            member.search_book()
            continue
        elif user_choice == 2 :
            member.display_all_book()
            print("please choose book : ")
            isbn = int(input("enter isbn number : "))
            member.issue_book(isbn)
            continue
        elif user_choice == 3:
            member.return_book()
            continue
        elif user_choice == 4:
            member.display_all_book()
            continue
        elif user_choice == 5:
            member.my_books()
            continue
        else:
            sys.exit()
    else:
        sys.exit()
