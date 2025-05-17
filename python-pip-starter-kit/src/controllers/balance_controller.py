
class BalanceController(object):

    def __init__(self, balance_service):
        self.balance_service = balance_service

    def showBalance(self, bank_name, borrower_name, emi, emi_no):
        return self.balance_service.showBalance(bank_name, borrower_name, emi, emi_no)
