from wtforms import StringField,PasswordField,SubmitField,EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,length,EqualTo

class Login(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('login')
    
    
class Signup(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    conferm = PasswordField('Confirmer_Password',validators=[DataRequired()])
    submit = SubmitField('SignUp')