from flask import render_template, request, redirect, url_for
from .payment_processor import PaymentProcessor

from app import app
from app.forms import PayForm


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()
    if request.method == 'POST' and form.validate_on_submit():
        amount = form.amount.data
        currency = form.currency.data
        description = form.description.data

        p = PaymentProcessor(amount, currency, description)
        p.processing()

        return redirect(url_for('submit'))
    return render_template('pay_form.html', title='Pay Form', form=form)


@app.route('/submit')
def submit():
    # TODO handle form processing
    return 'Accepted'
