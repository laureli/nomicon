from flask import Flask
from codes import db_login
app = Flask(__name__)

app.secret_key = 'development key'


# -------------- START MAIL SETTINGS -- REMOVE THIS 

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = email_username
# app.config["MAIL_PASSWORD"] = email_pw

# app.config["MAIL_DEFAULT_SENDER"] = email_username

# -------------- END MAIL SETTINGS -- REMOVE THIS 

# -------------- START DATABASE SETTINGS ----------------

app.config['SQLALCHEMY_DATABASE_URI'] = db_login
 
from models import db
db.init_app(app)

# -------------- END DATABASE SETTINGS ------------------

import nom_app.routes
