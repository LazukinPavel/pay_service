from flask import render_template, request, redirect, url_for
from .payment_processor import PaymentProcessor

from app import app
from app.forms import PayForm, PayFormProtocolPAY


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()

    if form.validate_on_submit():
        amount = form.amount.data
        form.amount.data = amount
        currency = form.currency.data
        description = form.description.data
        p = PaymentProcessor(amount, currency, description)
        processed_data = p.processing()
        # form = PayFormProtocolPAY(**processed_data)
        piastrix_url = 'https://pay.piastrix.com/ru/pay'
        return render_template('pay_1.html', title='Submit Form', action_url=piastrix_url, **processed_data)
    return render_template('pay_form.html', title='Pay Form', form=form)






