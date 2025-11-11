from time import time
class Loan:
    loan_id=0
    def __init__(self,book_id,member_id):
        self.id = Loan.loan_id
        Loan.loan_id+=1
        self.book_id = book_id
        self.member_id = member_id
        self.status = 'open'
        self.open_date = time()
        self.return_date = None
        
    def close_loan(self,return_date):
        if self.status != 'closed':
            self.return_date = return_date
            self.status = 'closed'