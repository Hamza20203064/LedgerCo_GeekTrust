# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT

from src.service.payment_services_interface import PaymentServiceInterface
from src.service.loan_services import LoanService


class PaymentService(PaymentServiceInterface):

    def addPayment(self, bank_name, user_name, lump_sum_amount, emi_no):
        user = LoanService().getUserDetails(bank_name, user_name)
        # this returns user_details  map (key is the user_id = bank_name + user_name)
        # value ---> object of user
        # user.getEMI().setLumpSumAmount(lump_sum_amount)
        # user.getEMI().setEMIno(emi_no)
        user.getEMI().modefiedEMIListAfertLumpSumPayment(lump_sum_amount, emi_no)
