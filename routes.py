from flask import Flask, render_template, request, flash
from forms import ContactForm, IngSearchForm, RecipeSearchForm, SignUpForm
from flask_mail import Message, Mail
from codes import email_username, email_pw
import mixpanel

# APPLICATION CONFIG
 
app = Flask(__name__)
 
app.secret_key = 'development key'

# -------------- START MAIL SETTINGS -- REMOVE THIS 
# mail = Mail(app)

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = email_username
# app.config["MAIL_PASSWORD"] = email_pw

# app.config["MAIL_DEFAULT_SENDER"] = email_username

# mail = Mail(app)
# -------------- END MAIL SETTINGS -- REMOVE THIS 


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
		    msg = Message(form.subject.data, sender='sample@sample.com', recipients=email_username)
		    msg.body = """
		    From: %s <%s>
		    %s
		    """ % (form.name.data, form.email.data, form.message.data)
		    mail.send(msg)
		    return render_template('contact.html', success=True)

	elif request.method == 'GET':
		return render_template('contact.html', form=form)


@app.route('/ingredient_search', methods=['GET', 'POST'])
def ing_search():
	form=IngSearchForm()

	if request.method == 'POST':
		if form.validate()== False:
			flash('please fill in all fields correctly')
			return render_template('ingredient_search.html', form=form)
		else:
			return "snap"

			# do the search
			# see above and figure it out. set up DB, datamodel etc.
	
	elif request.method == 'GET':
		return render_template('ingredient_search.html', form=form)
	else:
		return "sigh."


@app.route('/recipe_search', methods=['GET', 'POST'])
def recipe_search():
	form=RecipeSearchForm()

	if request.method == 'POST':
		if form.validate()== False:
			flash('please fill in all fields correctly')
			return render_template('recipe_search.html', form=form)
		else:
			return "snap"

	elif request.method == 'GET':
		return render_template('recipe_search.html', form=form)
	else:
		return "sigh."


  # //////////////  START TEST MAIL FEATURE ///////////////
@app.route("/mailtest")
def mailtest():

    msg = Message("Hello",
                  sender=email_username,
                  recipients=[email_username]
                  )
    mail.send(msg)
    return 'maybe your email got sent'
# //////////////  END TEST MAIL FEATURE ///////////////




if __name__=='__main__':
	app.run(debug=True)