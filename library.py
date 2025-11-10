from book import Book
from user import Member
from loan import Loan
from json_managment import FileManegment
import datetime
import csv

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = {}
        self.max_borrow_says = 14
        
    is_new_book = True
    def add_book(self,title,book):
        self.books[title] = book
        FileManegment.json_write('books.json',book)
    
    is_new_user = True
    def add_member(self,name,member):
        self.members[name] = member
        FileManegment.json_write('users.json',member)
       
    def borrow(self,book:Book,member:Member,date,loan:Loan):
        if self.books[book.title].get('id') is not None and self.members[member.full_name].get('id') is not None:
            print('exec borrow')
            self.loans[loan.open_date] = loan.__dict__
            book.mark_unavailable()
            member.increment_loans()
            member.borrow_book(book)
            
    def return_book(self,book:Book,member:Member,date,loan:Loan):
        if self.loans[loan.open_date].get('id') is not None and self.loans[loan.open_date].get('status') == 'open':
            member.decrement_loans()
            member.return_book(book)
            loan.close_loan(date)
            book.mark_available()
            
            
    def list_availble(self):
        return [book for book in self.books if self.books[book]['is_available']]
    
    def search_book(self,title):
        books = []
        for book in self.books:
            if book == title:
                books.append(self.books[title])
        return books
    

# create books
book_1 = Book(101,'harry potter','j.k rolling',True)
book_2 = Book(102,'the hobbit','tolkin',True)
book_3 = Book(103,'lord of the rings','tolkin',True)

# create members
member_1 = Member(101,'baruch lavy',0)
member_2 = Member(102,'michal lavy',0)

# create liberary
library = Library()

# add books
library.add_book(book_1.title,book_1.__dict__)
library.add_book(book_2.title,book_2.__dict__)
library.add_book(book_3.title,book_3.__dict__)
# print(library.books)

# add members
library.add_member(member_1.full_name,member_1.__dict__)
library.add_member(member_2.full_name,member_2.__dict__)
# print(library.members)

# create loans
loan_1 = Loan(101,book_1.id,member_1.id,datetime.datetime.now())
loan_2 = Loan(102,book_2.id,member_1.id,datetime.datetime.now())
# print(loan_1.__dict__)

# execute_loans
library.borrow(book_1,member_1,datetime.datetime.now(),loan_1)
library.borrow(book_2,member_1,datetime.datetime.now(),loan_2)
# print(library.loans)
# print(book_1.__dict__)

# returning book
library.return_book(book_1,member_1,datetime.datetime.now(),loan_1)
# print(f'after {library.loans}')

# print(library.search_book('harry potter'))
# print(library.books)
# print(library.list_availble())