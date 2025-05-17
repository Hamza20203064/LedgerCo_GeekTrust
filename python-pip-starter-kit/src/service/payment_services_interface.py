# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT


import abc  # abstract base class


class PaymentServiceInterface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def addPayment(self, bank_name, user_name, lump_sum_amount, emi_no):
        pass
