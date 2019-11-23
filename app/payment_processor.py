import hashlib
import random

from flask import current_app


currency_codes = {
    'eur': 978,
    'usd': 840,
    'rur': 643
}


class PaymentProcessor:
    def __init__(self, amount, currency, description):
        self.amount = "{0:.2f}".format(amount)
        self.currency = currency
        self.description = description

    def processing(self):
        if self.currency == '978':
            return self._process_eur()
        # if self.currency == 840:
        #     self._process_usd()
        # if self.currency == 643:
        #     self._process_rur()

    def _process_rur(self):
        pass

    def _process_usd(self):
        pass

    def _process_eur(self):
        keys_required = ['amount', 'currency', 'shop_id', 'shop_order_id']
        params = {
            'amount': self.amount,
            'currency': self.currency,
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000)
        }
        sign = self.get_sign(params, keys_required)
        params['sign'] = sign
        return params

    def get_sign(self, params, keys_required):
        keys_sorted = sorted(keys_required)
        values = [str(params[k]) for k in keys_sorted]
        pre_hash = ':'.join(values)
        pre_hash += current_app.config['SECRET_KEY']
        # print(pre_hash)
        sign = hashlib.sha256(pre_hash.encode()).hexdigest()
        return sign

