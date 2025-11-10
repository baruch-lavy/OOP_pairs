from book import Book
import json
from json_managment import FileManegment
class Member:
    def __init__(self,id,full_name,active_loans_count=0):
        self.id = id
        self.full_name = full_name
        self.loans = active_loans_count
        self.borrowed_books:list[Book] = []
    
    def borrow_book(self,book:Book):
        self.borrowed_books.append(book)
        with open('users.json','r') as f:
            data = json.load(f)
            for user in data:
                if user['id'] == self.id:
                    user['borrowed_books'].append(book.__dict__)
                    
            FileManegment.json_write('users.json',data,True)
        
    def return_book(self,book:Book):
        self.borrowed_books.remove(book)
       
    def increment_loans(self):
        self.loans += 1
        
    def decrement_loans(self):
        if (self.loans - 1) < 0:
            self.loans = 0
        else:   
            self.loans -= 1
