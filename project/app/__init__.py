from flask import Flask
app = Flask(__name__)

##
#register blueprints
##

from app.blueprints.home_blueprint import home
app.register_blueprint(account)

from app.blueprints.account_blueprint import account
app.register_blueprint(account)


