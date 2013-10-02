from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

#  //////////////// user management forms
class ContactForm(Form):
	name = TextField('Name', [validators.Required('please enter your name.')])
	email = TextField('Email', [validators.Required('please enter your email.'), validators.Email('please enter your email.')])
	subject = TextField('Subject', [validators.Required('please enter a subject.')])
	message = TextAreaField('Message', [validators.Required('please enter your msg.')])
	submit = SubmitField('Send')

#  //////////////// searching forms
class IngSearchForm(Form):
	ingredient = TextAreaField('ingredients:', 
		[validators.Required('please enter at least 1 ingredient. you can separate them with spaces or commas.')])
	ing_submit = SubmitField('search')


class RecipeSearchForm(Form):
	recipe = TextAreaField('recipe terms:', 
		[validators.Required('please enter 1+ terms that might be in the recipe name.')])
	rec_submit = SubmitField('search')



class SignUpForm(Form):
	firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
	lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create account")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if note Form.validate(self):
			return False

		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True