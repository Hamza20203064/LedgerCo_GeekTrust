
class PaymentController(object):

    def __init__(self, payment_service):
        self.payment_service = payment_service

    def addPayment(self, bank_name, user_name, lump_sum_amount, emi_no):
        self.payment_service.addPayment(
            bank_name, user_name, lump_sum_amount, emi_no)
