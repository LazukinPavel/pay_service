import hashlib
import random


currency_codes = {
    'eur': 978,
    'usd': 840,
    'rur': 643
}


class PaymentProcessor:
    def __init__(self, amount, currency, description, shop_id):
        self.amount = amount
        self.currency = currency_codes[currency]
        self.description = description
        self.shop_id = shop_id

    def processing(self):
        if self.currency == 978:
            self._process_eur()
        if self.currency == 840:
            self._process_usd()
        if self.currency == 643:
            self._process_rur()

    def _process_rur(self):
        pass

    def _process_usd(self):
        pass

    def _process_eur(self):
        keys_required = ['amount', 'currency', 'shop_id', 'shop_order_id']
        params = {
            'amount': self.amount,
            'currency': self.currency,
            'shop_id': self.shop_id,
            'shop_order_id': random.randrange(10000)
        }




    def get_sign(self, params, keys_required):
        # params = {
        #     "currency": "643",
        #     "payway": "payeer_rub",
        #     "amount": "12.34",
        #     "shop_id": "5",
        #     "shop_order_id": 4126,
        #     "description": "Test invoice",
        # }
        # keys_required = ("shop_id", "payway", "amount", "currency", "shop_order_id")

        keys_sorted = sorted(keys_required)
        values = [str(params[k]) for k in keys_sorted]
        pre_hash = ':'.join(values)
        sign = hashlib.sha256(pre_hash.encode('utf-8')).hexdigest()
        return sign

