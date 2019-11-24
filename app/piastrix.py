import hashlib
import random
import requests

from flask import current_app


class Piastrix:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def request_piastrix(self, url, fields):
        try:
            resp = requests.post(url, json=fields).json()
            print('=== resp', resp)
        except requests.exceptions.ConnectionError as e:
            current_app.logger.error(e)
            return None
        return resp

    def prepare_form_fields(self):
        if self.currency == '978':
            fields, keys_required = self._prepare_data_eur()
        elif self.currency == '840':
            fields, keys_required = self._prepare_data_usd()
        else:
            fields, keys_required = self._prepare_data_rur()

        sign = self._get_sign(fields, keys_required)
        fields['sign'] = sign
        return fields

    def _prepare_data_rur(self):
        keys_required = ['amount', 'currency', 'payway', 'shop_id', 'shop_order_id']
        fields = {
            'amount': self.amount,
            'currency': self.currency,
            'payway': 'payeer_rub',
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000)
        }
        return fields, keys_required

    def _prepare_data_usd(self):
        keys_required = ['shop_amount', 'shop_currency', 'shop_id', 'shop_order_id', 'payer_currency']
        fields = {
            'shop_amount': self.amount,
            'shop_currency': self.currency,
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000),
            'payer_currency': self.currency
        }
        return fields, keys_required

    def _prepare_data_eur(self):
        keys_required = ['amount', 'currency', 'shop_id', 'shop_order_id']
        fields = {
            'amount': self.amount,
            'currency': self.currency,
            'shop_id': current_app.config['SHOP_ID'],
            'shop_order_id': random.randrange(10000)
        }
        return fields, keys_required

    def _get_sign(self, fields, keys_required):
        keys_sorted = sorted(keys_required)
        values = [str(fields[k]) for k in keys_sorted]
        pre_hash = ':'.join(values)
        pre_hash += current_app.config['SECRET_KEY']
        sign = hashlib.sha256(pre_hash.encode()).hexdigest()
        return sign

