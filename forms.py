#from flask_wtf import *
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
#from wtforms import *

class ContactForm(Form):
	name = TextField("Name of Student", [validators.InputRequired (message="Please enter your name.")])
	Gender = RadioField('Gender',choices=[('M','Male'),('F','Female')])
	Address = TextAreaField("Address")
	email = TextField("Email", [validators.InputRequired (message="Please enter your email address"), validators.Email("Please enter your valid email")])
	Age = IntegerField("Age")
	language = SelectField('Language', choices = [('cpp','C++'), ('py', 'Python')])
	submit = SubmitField("Send")



