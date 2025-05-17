from src.service.loan_services_inerface import LoanServiceInerface
from src.model.user import User


class LoanService(LoanServiceInerface):
    # Dictionary to store user details--> as I  am not using db.
    user_details = {}

    def createLoan(self, bank_name, borrower_name, principal_amount, no_of_years, interest_rate):

        # defining userFunction
        user = User(bank_name, borrower_name, principal_amount,
                    no_of_years, interest_rate)

        self.__class__.user_details[user.getUserId()] = user
        return user

    def getUserDetails(self, bank_name, borrower_name):

        user_id = bank_name + borrower_name
        if user_id in self.__class__.user_details:
            return self.__class__.user_details[user_id]
        else:
            return ("User does not exist")
