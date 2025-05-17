
from src.service.loan_services import LoanService
from src.service.payment_services import PaymentService
from src.service.balance_services import BalanceService
from src.model.emi import EMI
from src.model.user import User
from src.controllers.loan_controller import LoanController
from src.controllers.balance_controller import BalanceController
from src.controllers.payment_controllers import PaymentController


class Main(object):
    def app(self, input_list):
        # Create instances of the services
        loan_service = LoanService()
        payment_service = PaymentService()
        balance_service = BalanceService()

        # Create instances of the controllers
        loan_controller = LoanController(loan_service)
        balance_controller = BalanceController(balance_service)
        payment_controller = PaymentController(payment_service)
        results = []
        for command in input_list:
            command = command.split()
            # print(command[0])
            if command[0] == "LOAN":
                # Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
                bank_name = command[1]
                borrower_name = command[2]
                principal_amount = int(command[3])
                no_of_years = int(command[4])
                interest_rate = float(command[5])
                loan_controller.createLoan(
                    bank_name, borrower_name, principal_amount, no_of_years, interest_rate)
            elif command[0] == "PAYMENT":
                # Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO
                bank_name = command[1]
                borrower_name = command[2]
                lump_sum_amount = int(command[3])
                emi_no = int(command[4])
                payment_controller.addPayment(
                    bank_name, borrower_name, lump_sum_amount, emi_no)
                # print("Payment added successfully")
            elif command[0] == "BALANCE":
                # Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
                bank_name = command[1]
                borrower_name = command[2]
                emi_no = int(command[3])
                emi = loan_service.getUserDetails(
                    bank_name, borrower_name).getEMI()
                result = balance_controller.showBalance(
                    bank_name, borrower_name, emi, emi_no)
                results.append(result)
            else:
                return ("Invalid command")
            
        return results
  

    def startApp(self,Lines):
        results = self.app(Lines)
        for result in results:
            print(*result)