from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange


class PayForm(FlaskForm):
    amount = DecimalField(
        'Payment amount',
        places=2,
        validators=[NumberRange(min=0.01), DataRequired(message='Invalid input')],
    )
    currency = SelectField('Currency', choices=[('978', 'EUR'), ('usd', 'USD'), ('rur', 'RUR')])
    description = TextAreaField('Product Description')
    submit = SubmitField('OK')


class PayFormProtocolPAY(FlaskForm):
    amount = HiddenField(description='amount')
    currency = HiddenField(description='currency')
    shop_id = HiddenField(description='shop_id')
    sign = HiddenField(description='sign')
    shop_order_id = HiddenField(description='shop_order_id')
    description = HiddenField(description='description')
    submit = SubmitField('Submit')

