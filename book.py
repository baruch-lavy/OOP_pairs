class Book:
    id_book=1
    def __init__(self,title,author,is_available=True):
        self.id = Book.id_book
        Book.id_book+=1
        self.title = title
        self.author = author
        self.is_available = is_available
        
    def mark_unavailable(self):
        if self.is_available == True:
            self.is_available = False
        
    def mark_available(self):
        self.is_available = True
        