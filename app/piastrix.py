import hashlib
import random

from flask import current_app


class Piastrix:
    def __init__(self, amount, currency, description):
        self.amount = "{0:.2f}".format(amount)
        self.currency = currency
        self.description = description

    def processing(self):
        if self.currency == '978':
            params, keys_required = self._process_eur()
        elif self.currency == '840':
            params, keys_required = self._process_eur()
        else:
            params, keys_required = self._process_eur()

        sign = self._get_sign(params, keys_required)
        params['sign'] = sign
        return params

    def _process_rur(self):
        keys_required = ['amount', 'currency', 'payway', 'shop_id', 'shop_order_id']
        params = {
            'amount': self.amount,
            'currency': self.currency,
            'payway': 'payeer_rub',
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000)
        }
        return params, keys_required

    def _process_usd(self):
        keys_required = ['shop_amount', 'shop_currency', 'shop_id', 'shop_order_id', 'payer_currency']
        params = {
            'shop_amount': self.amount,
            'shop_currency': self.currency,
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000),
            'payer_currency': self.currency
        }
        return params, keys_required

    def _process_eur(self):
        keys_required = ['amount', 'currency', 'shop_id', 'shop_order_id']
        params = {
            'amount': self.amount,
            'currency': self.currency,
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000)
        }
        return params, keys_required

    def _get_sign(self, params, keys_required):
        keys_sorted = sorted(keys_required)
        values = [str(params[k]) for k in keys_sorted]
        pre_hash = ':'.join(values)
        pre_hash += current_app.config['SECRET_KEY']
        sign = hashlib.sha256(pre_hash.encode()).hexdigest()
        return sign

