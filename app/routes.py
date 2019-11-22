from flask import render_template, request, redirect, url_for
from .payment_processor import PaymentProcessor

from app import app
from app.forms import PayForm, PayFormProtocolPAY


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()
    if request.method == 'POST' and form.validate_on_submit():
        amount = form.amount.data
        currency = form.currency.data
        description = form.description.data

        p = PaymentProcessor(amount, currency, description, app.config['SHOP_ID'])
        p.processing()

        return redirect(url_for('submit'))
    return render_template('pay_form.html', title='Pay Form', form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = PayFormProtocolPAY()
    if request.method == 'POST' and form.validate_on_submit():

        # TODO pass form-data to piastrix
        return redirect('https://pay.piastrix.com/en/pay')

    return render_template('pay_form.html', title='Pay Form', form=form)
