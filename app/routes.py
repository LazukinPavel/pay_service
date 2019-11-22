from flask import render_template, request, redirect, url_for
from .payment_processor import PaymentProcessor

from app import app
from app.forms import PayForm, PayFormProtocolPAY


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()
    if request.method == 'POST' and form.validate_on_submit():
        # print(form.__dict__)
        amount = form.amount.data
        currency = form.currency.data
        description = form.description.data
        return redirect(url_for('success'))
    return render_template('pay_form.html', title='Pay Form', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    form = PayFormProtocolPAY(amount=123)
    if request.method == 'POST' and form.validate_on_submit():
        # print('=== req', request.__dict__)
        # p = PaymentProcessor(amount, currency, description, app.config['SHOP_ID'])
        # processed_data = p.processing()
        # TODO pass form-data to piastrix
        return redirect('https://pay.piastrix.com/en/pay', code=307)
    return render_template('pay_form.html', title='Submit Form', form=form)
