from flask_wtf import FlaskForm
from wtforms import DecimalField, TextAreaField, SubmitField, SelectField, HiddenField
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


class PayFormProtocolPAY(FlaskForm):
    currency = HiddenField(description='currency')
    shop_id = HiddenField(description='shop_id')
    sign = HiddenField(description='sign')
    shop_order_id = HiddenField(description='shop_order_id')
    submit = SubmitField('Submit')




# <form name="Pay" method="post" action=" https://pay.piastrix.com/ru/pay"
# accept-charset="UTF-8>
# <input type="hidden" name="amount" value="10.00"/>
# <input type="hidden" name="currency" value="643"/>
# <input type="hidden" name="shop_id" value="5"/>
# <input type="hidden" name="sign"
# value="e4580435a252d61ef91b71cb23ed7bee4d77de94ced36411526d2ce3b6
# 6ada8f"/>
# <input type="hidden" name="shop_order_id" value="101"/>
# <input type="submit" input type="hidden" name="description" value="Test
# invoice"/>
# </form>