class Loan:
    def __init__(self,id,book_id,member_id,open_date,return_date=None):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.status = 'open'
        self.open_date = open_date
        self.return_date = return_date
        
    def close_loan(self,return_date):
        if self.status != 'closed':
            self.return_date = return_date
            self.status = 'closed'