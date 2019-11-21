from flask import render_template, request

from app import app
from app.forms import PayForm


@app.route('/', methods=['GET', 'POST'])
def pay_form():
    form = PayForm()
    return render_template('pay_form.html', title='Pay Form', form=form)


@app.route('/submit')
def submit():
    form = PayForm(request.form)
    if request.method == 'POST' and form.validate():
        print('=== Form accepted')
        # TODO handle form processing

