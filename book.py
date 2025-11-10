class Book:
    def __init__(self,title,auther,isbn,is_available=True):
        self.title=title
        self.auther=auther
        self.isbn=isbn
        self.is_available=is_available
    
    def get_details(self) -> str :
        stri=""
        stri+=self.title
        stri+=self.auther
        stri+=self.isbn
        return stri,self.is_available