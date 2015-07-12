from flask import Blueprint

account = Blueprint('account', __name__)


@account.route("/account/signup")
def signup():
    pass

@account.route("/account/signin")
def signin():
    pass

