from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
from codes import email_username, email_pw
import mixpanel

# APPLICATION CONFIG
mail = Mail()
 
app = Flask(__name__)
 
app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = email_username
app.config["MAIL_PASSWORD"] = email_pw
 
mail.init_app(app)

# APPLICATION ORGANIZATION

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

# how do i want to transfer msgs?
@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form =ContactForm()

	if request.method == 'POST':
		if form.validate()== False:
			flash('please fill in all fields correctly')
			return render_template('contact.html', form=form)
		else:
			msg=Message(form.subject.data, sender='sender-contact@example.com', recipients=['recip@example.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" %(form.name.data, form.email.data, form.message.data)
			mail.send(msg)

			return render_template('contact.html', success=True)

	elif request.method == 'GET':
		return render_template('contact.html', form=form)

if __name__=='__main__':
	app.run(debug=True)