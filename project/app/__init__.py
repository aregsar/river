from flask import Flask
app = Flask(__name__)




#blueprints
from app.blueprints.account_blueprint import account
if True:#todo: add feature flag support for registering blueprints
    app.register_blueprint(account)

#leave this comment in for adding blueprints via river cli
##blueprints
