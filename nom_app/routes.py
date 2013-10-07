from nom_app import app
from flask import render_template, request, flash, session, url_for, redirect, g
from forms import ContactForm, IngSearchForm, RecipeSearchForm, SignUpForm, SignInForm
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask_mail import Message, Mail
from codes import email_username, email_pw
from models import db, User

# APPLICATION CONFIG
 
mail = Mail()

################  START APPLICATION ORGANIZATION ###############

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

################  END APPLICATION ORGANIZATION ###############

############### Start LoginHandler settings ###############

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

@lm.user_loader
def load_user(id):
    return dbsession.query(User).get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    # this is used as 'current_user.id' or 'current_user.email'
   

############### End LoginHandler settings ###############

################  START USER MANAGEMENT ///////////////

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()

  if 'email' in session:
    return redirect(url_for('profile')) 
  
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      
      session['email'] = newuser.email
      return redirect(url_for('profile'))
  
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/profile')
def profile():

	if 'email' not in session:
		return redirect(url_for('signin'))

	user = User.query.filter_by(email = session['email']).first()

	if user is None:
		return redirect(url_for('signin'))
	else:
		return render_template('profile.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	form = SignInForm()

	if 'email' in session:
		return redirect(url_for('profile'))
   
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signin.html', form=form)
		else:
			session['email'] = form.email.data
			return redirect(url_for('profile'))

	elif request.method == 'GET':
		return render_template('signin.html', form=form) 

@app.route('/signout')
def signout():
	if 'email' not in session:
		return redirect (url_for('signin'))

	session.pop('email', None)
	return redirect(url_for('home'))

################  END USER MANAGEMENT ///////////////

################  START YUMMLY SEARCHING ///////////////

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

################  END YUMMLY SEARCHING ///////////////

################  START DATABASE TEST ///////////////

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'it works, cools!'
	else:
		return 'something is broken.'

################  END DATABASE TEST ///////////////


################  START TEST MAIL FEATURE ///////////////
@app.route("/mailtest")
def mailtest():

    msg = Message("Hello",
                  sender=email_username,
                  recipients=[email_username]
                  )
    mail.send(msg)
    return 'maybe your email got sent'


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

################  END TEST MAIL FEATURE ///////////////


if __name__=='__main__':
	app.run(debug=True)