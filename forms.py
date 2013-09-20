from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

#  //////////////// user management forms
class ContactForm(Form):
	name = TextField('Name', [validators.Required('please enter your name.')])
	email = TextField('Email', [validators.Required('please enter your email.'), validators.Email('please enter your email.')])
	subject = TextField('Subject', [validators.Required('please enter a subject.')])
	message = TextAreaField('Message', [validators.Required('please enter your msg.')])
	submit = SubmitField('Send')

class SignUpForm(Form):
	pass

#  //////////////// searching forms
class IngSearchForm(Form):
	# ingredient = TextField('Ingredients', [validators.Required('please enter at least 1 ingredient. \n you can separate them with spaces or commas.')])
	ingredient = TextAreaField('Ingredients', [validators.Required('please enter at least 1 ingredient. \n you can separate them with spaces or commas.')])

	submit = SubmitField('Search')

