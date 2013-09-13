from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField('Name', [validators.Required('please enter your name.')])
	email = TextField('Email', [validators.Required('please enter your email'), validators.Email('please enter your email')])
	subject = TextField('Subject', [validators.Required('please enter a subject')])
	message = TextAreaField('Message', [validators.Required('please enter your msg')])
	submit = SubmitField('Send')
