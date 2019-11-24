from datetime import datetime

from flask import render_template, redirect
from .piastrix import Piastrix

from app import app
from app.forms import PayForm


@app.route('/', methods=['GET', 'POST'])
def root():
    form = PayForm()

    if form.validate_on_submit():
        amount = form.amount.data
        amount = "{0:.2f}".format(amount)
        currency = form.currency.data
        description = form.currency.description

        piastrix = Piastrix(amount, currency)
        fields = piastrix.prepare_form_fields()

        app.logger.info(
            f'Incoming payment received.\n'
            f'Time: {datetime.now()}\n'
            f'Order ID: {fields["shop_order_id"]}\n'
            f'Amount: {amount}\n'
            f'Currency code: {currency}\n'
            f'Description: {description if description else "No description specified"}\n'
            f'======'
        )

        # Direct
        if currency == '978':
            pay_url = 'https://pay.piastrix.com/ru/pay'
            return render_template('form_direct.html', title='Direct', action_url=pay_url, fields=fields)

        # Bill
        elif currency == '840':
            create_bill_url = 'https://core.piastrix.com/bill/create'
            resp = piastrix.request_piastrix(create_bill_url, fields)
            if not resp:
                return render_template('error.html', message='Connection error')
            if not resp['result']:
                app.logger.info(
                    f'Piastrix error: {resp["message"]}, error code {resp["error_code"]}'
                )
                return render_template('error.html', message=resp['message'])
            else:
                pay_url = resp['data']['url']
                return redirect(pay_url)

        # Invoice
        else:
            create_invoice_url = 'https://core.piastrix.com/invoice/create'
            resp = piastrix.request_piastrix(create_invoice_url, fields)
            if not resp:
                return render_template('error.html', message='Connection error')
            if not resp['result']:
                app.logger.info(
                    f'Piastrix error: {resp["message"]}, error code {resp["error_code"]}'
                )
                return render_template('error.html', message=resp['message'])
            else:
                method = resp['data']['method']
                pay_url = resp['data']['url']
                fields = resp['data']['data']
                return render_template(
                    'form_invoice.html',
                    title='Invoice',
                    action_url=pay_url,
                    fields=fields,
                    method=method
                )

    return render_template('form_initial.html', form=form)

