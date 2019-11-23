from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class PayForm(FlaskForm):
    amount = DecimalField(
        'Payment amount',
        places=2,
        validators=[NumberRange(min=0.01), DataRequired(message='Invalid input')],
    )
    currency = SelectField('Currency', choices=[('978', 'EUR'), ('840', 'USD'), ('643', 'RUR')])
    description = TextAreaField('Product Description')
    submit = SubmitField('Submit')


