# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT


# Interface
import abc  # abstract base class


class BalaServiceInerface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def showBalance(self, bank_name, borrower_name, emi, emi_no):
        pass
