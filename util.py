from wtforms import Form,StringField,SelectField
class TickerForm(Form):

    choices = [('1d', '1d'),
            ('5d', '5d'),
            ('1mo', '1mo'),
            ('1y', '1y'),
            ('ytd', 'ytd'),
            ('max', 'max')]
    search = StringField('')
    select = SelectField('Period',choices=choices)
