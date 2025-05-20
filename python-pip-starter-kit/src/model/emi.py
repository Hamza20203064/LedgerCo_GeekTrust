# Format - LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST
# Format - PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO

# Input format - BALANCE BANK_NAME BORROWER_NAME EMI_NO
# Output format - BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT
import math


class EMI(object):
    def __init__(self, user_id, total_amount, no_of_installments):
        self.user_id = user_id
        self.total_amount = total_amount
        self.no_of_installments = no_of_installments
        self.monthly_installment = self.calculateMonthlyInstallment()
        self.emi_list0 = [0] + [self.monthly_installment] * (no_of_installments - 1)
        self.emi_list = self.emi_list0 + [self.getLastBill()]
        self.no_of_installments_left = no_of_installments

        # self.lump_sum_amount = self.getLumpSumAmount()
        # self.emi_no = None

    def getLastBill(self):
        last_balance = self.total_amount - sum(self.emi_list0) 
        return int(last_balance)
        

    def setTotalAmount(self, total_amount):
        self.total_amount = total_amount

    def getTotalAmount(self):
        return self.total_amount

    def setEmiNo(self, no_of_installments):
        self.no_of_installments = no_of_installments

    def getEmiNo(self):
        return self.no_of_installments

    def calculateMonthlyInstallment(self):
        monthly_installment = math.ceil(
            self.total_amount / self.no_of_installments)
        return monthly_installment

    def getNoOfEmisLeftAndAmountPaid(self, emi_no):
        if emi_no + 1 > len(self.emi_list):
            return "Invalid EMI number"

        amount_paid = 0
        amount_left_to_pay = self.total_amount
        for i in range(emi_no + 1):
            amount_paid += self.emi_list[i]
            amount_left_to_pay -= self.emi_list[i]

        no_of_installments_left = self.getNoOfInstallmentsLeft(
            amount_left_to_pay)

        return amount_paid, no_of_installments_left

    def getNoOfInstallmentsLeft(self, amount_left_to_pay):
        return math.ceil(amount_left_to_pay / self.monthly_installment)

    def getEMIList(self):
        return self.emi_list

    # def setLumpSumAmount(self, lump_sum_amount):
    #     self.lump_sum_amount = lump_sum_amount

    # def getLumpSumAmount(self):
    #     return self.lump_sum_amount

    # def setEMIno(self, emi_no):
    #     self.emi_no = emi_no

    # def gitEMIno(self):
    #     return self.emi_no

    def modefiedEMIListAfertLumpSumPayment(self, lump_sum_amount, emi_no):
        if emi_no > len(self.emi_list):
            print("All installments are already completed.")
        else:
            remaining_amount = 0
            for i in range(emi_no, len(self.emi_list)):
                remaining_amount += self.emi_list[i]
            if remaining_amount < lump_sum_amount:
                print("HOLD ON! You are going to pay some extra amount.")
            else:
                self.emi_list[emi_no] += lump_sum_amount
                while lump_sum_amount >= self.emi_list[len(self.emi_list) - 1]:
                    lump_sum_amount -= self.emi_list[len(self.emi_list) - 1]
                    self.emi_list.pop()
                self.emi_list[len(self.emi_list) -1] -= lump_sum_amount
