# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

from src.model.emi import EMI


class User(object):
    def __init__(self, bank_name, borrower_name, principal_amount, no_of_years, interest_rate):
        self.borrower_name = borrower_name
        self.principal_amount = principal_amount
        self.no_of_years = no_of_years
        self.interest_rate = interest_rate
        self.total_amount = self.calculateTotalAmount()
        self.no_of_installments = no_of_years * 12
        self.user_id = bank_name + borrower_name
        self.emi = EMI(self.user_id,  self.total_amount,
                       self.no_of_installments)

    def getUserId(self):
        return self.user_id

    def setEMI(self, emi):
        self.emi = emi

    def getEMI(self):
        return self.emi

    def setBorrowerName(self, borrower_name):
        self.borrower_name = borrower_name

    def getBorrowerName(self):
        return self.borrower_name

    def setPrincipalAmount(self, principal_amount):
        self.principal_amount = principal_amount

    def getPrincipalAmount(self):
        return self.principal_amount

    def setInterestRate(self, interest_rate):
        self.interest_rate = interest_rate

    def getInterestRate(self):
        return self.interest_rate

    def setNoOfYears(self, no_of_years):
        self.no_of_years = no_of_years

    def getNoOfYears(self):
        return self.no_of_years

    def setTotalAmount(self, total_amount):
        self.total_amount = total_amount

    def getTotalAmount(self):
        return self.total_amount

    def calculateTotalAmount(self):
        total_amount = self.principal_amount + \
            (self.principal_amount * (self.interest_rate / 100) * self.no_of_years)
        return total_amount
