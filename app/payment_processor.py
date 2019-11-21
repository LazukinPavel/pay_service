
class PaymentProcessor:
    def __init__(self, amount, currency, description):
        self.amount = amount
        self.currency = currency
        self.description = description

    def processing(self):
        if self.amount == 'EUR':
            self._process_eur()
        if self.amount == 'USD':
            self._process_usd()
        if self.amount == 'RUR':
            self._process_rur()

    def _process_rur(self):
        pass

    def _process_usd(self):
        pass

    def _process_eur(self):
        pass
