from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


# TODO inputs validation

class PayForm(FlaskForm):
    amount = DecimalField(
        'Payment amount',
        places=2,
        validators=[NumberRange(min=0.00), DataRequired(message='Invalid input')],
    )
    currency = SelectField('Currency', choices=[('eur', 'EUR'), ('usd', 'USD'), ('rur', 'RUR')])
    description = TextAreaField('Product Description')
    submit = SubmitField('Submit')
