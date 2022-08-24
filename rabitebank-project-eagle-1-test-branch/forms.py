from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length



# ONLINE TURN FORM
class OnlineForm(FlaskForm):
    filial = SelectField(label='Filial', choices=[('Bas ofis (Piramida plaza 1-ci mertebe)'), ('Nesimi filiali (Heyder Eliyev sarayinin yani)'), ('Buta filiali (Amerika sefirliyinin yani)'), ('Kaspian filiali (Kaspian plazanin 1-ci mertebesi)')])
    xidmet = SelectField(label='Xidmet novu', choices=[('Western Union'), ('Barat'), ('Onlayn kreditler'), ('Lombard krediti'), ('Kart sifarisi'), ('Kartin tehvil alinmasi')])
    date = DateField(label='Tarix', format="%Y-%m-%d", validators=[DataRequired()])
    mobile_num = StringField(label='Mobil nomre', validators=[DataRequired(), Length(min=4, max=25)])

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")

