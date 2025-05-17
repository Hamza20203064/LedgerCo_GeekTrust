# Interface
import abc  # abstract base class


class LoanServiceInerface(metaclass=abc.ABCMeta):  # interface
    @abc.abstractmethod  # daputer in python
    def createLoan(self, bank_name, borrower_name, principal_amount, no_of_years, interest_rate):
        pass

    @abc.abstractmethod  # daputer in python
    def getUserDetails(self, bank_name, borrower_name):
        pass
