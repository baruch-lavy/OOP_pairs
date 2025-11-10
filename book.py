class Book:
    def __init__(self,id,title,author,is_available=True):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = is_available
        
    def mark_unavailable(self):
        if self.is_available == True:
            self.is_available = False
        
    def mark_available(self):
        self.is_available = True