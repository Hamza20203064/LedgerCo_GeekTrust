# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

from src.service.balance_services_inerface import BalaServiceInerface
from src.model.emi import EMI
from src.model.user import User


class BalanceService(BalaServiceInerface):

    def showBalance(self, bank_name, borrower_name, emi, emi_no):
        if emi_no > len(emi.emi_list):
            return "Invalid EMI number"

        amount_paid, no_of_installments_left = emi.getNoOfEmisLeftAndAmountPaid(
            emi_no)

        return [bank_name, borrower_name, str(amount_paid), str(no_of_installments_left)]
