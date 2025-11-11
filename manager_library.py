
from OOP_pairs.library import Library
from OOP_pairs.library import Member
from OOP_pairs.library import Book
from OOP_pairs.library import Loan
from time import time

class Manager_library:
    def __init__(self):
        pass
    id_member=1
    def manager_library(self):
        library=Library()
        while True:    
            choose_reader=input(f"press 1 to resign \n just if you member in this library: \n press 2 to loan book \n press 3 to return a book \n press 4 to add new book to library \n press 5 to search book \n press 9 to exit")
            name=input("write your name")
            if choose_reader=='1':   
                for member in library.members:
                    if name in member:
                        print("user exist")
                    continue
                id_member=Manager_library.id_member
                Manager_library.id_member+=1
                member=Member(id_member,name)
                library.add_member(name,member.__dict__)
            
            elif choose_reader=='2':
                print(library.list_availble())
                choose_book=input("choose a book")
                book=library.books[choose_book]
                member=library.members[name]
                loan=Loan(book.id,member.id)
                library.borrow(book,member,loan)
            
            elif choose_reader=='3':
                book_return=input("write name book you return")
                date=time()
                library.return_book(book_return,member,date,loan)
            
            elif choose_reader=='4':
                name_book=input("write name book you add")
                auther_book=input("write name auther of book you add")
                book=Book(name_book,auther_book)
                library.add_book(name_book,book.__dict__)
            
            elif choose_reader=='5':
                name_book=input("write name book you search")
                if name_book in library.books:
                    print("the book is availble")
                else:
                    print("the book is not availble")
           
            elif choose_reader=='9':
                print("have a nice day")
                return
           
            else:
                print("wrong choise")

manager_library=Manager_library()
manager_library.manager_library()