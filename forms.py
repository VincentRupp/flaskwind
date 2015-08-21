from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateField
from wtforms.validators import DataRequired

STATE_ABBREV = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD', 
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class InputForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    state = StringField('state', default='IA',validators=[DataRequired()])
    from_date = DateField('from_date',validators=[DataRequired()])
    to_date = DateField('to_date',validators=[DataRequired()])