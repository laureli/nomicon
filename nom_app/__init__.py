from flask import Flask

app = Flask(__name__)

import nom_app.routes

app.secret_key = 'development key'

# -------------- START MAIL SETTINGS -- REMOVE THIS 

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = email_username
# app.config["MAIL_PASSWORD"] = email_pw

# app.config["MAIL_DEFAULT_SENDER"] = email_username

# -------------- END MAIL SETTINGS -- REMOVE THIS 

