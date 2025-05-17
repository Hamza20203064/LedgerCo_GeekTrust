
class LoanController(object):
    def __init__(self, loan_service):
        self.loan_service = loan_service

    def createLoan(self, bank_name, borrower_name, principal_amount, no_of_years, interest_rate):
        return self.loan_service.createLoan(bank_name, borrower_name, principal_amount, no_of_years, interest_rate)

    def getUserDetails(self, user_id):
        return self.loan_service.getUserDetails(user_id)
