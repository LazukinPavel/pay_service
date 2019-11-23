from flask import render_template, redirect
from .piastrix import Piastrix

from app import app
from app.forms import PayForm


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()

    if form.validate_on_submit():
        amount = form.amount.data
        form.amount.data = amount
        currency = form.currency.data
        piastrix = Piastrix(amount, currency)
        fields = piastrix.prepare_form_fields()

        # Direct
        if currency == '978':
            pay_url = 'https://pay.piastrix.com/ru/pay'
            return render_template('form_direct.html', title='Direct', action_url=pay_url, fields=fields)

        # Bill
        elif currency == '840':
            create_bill_url = 'https://core.piastrix.com/bill/create'
            resp = piastrix.request_piastrix(create_bill_url, fields)
            if not resp['result']:
                # TODO log error_code & message
                return resp['message']
            else:
                pay_url = resp['data']['url']
                return redirect(pay_url)

        # Invoice
        else:
            create_invoice_url = 'https://core.piastrix.com/invoice/create'
            resp = piastrix.request_piastrix(create_invoice_url, fields)
            if not resp['result']:
                # TODO log error_code & message
                return resp['message']
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






