from flask import Blueprint

home = Blueprint('home', __name__)


@home.route("/")
def index():
    return "Replace this text with your tagline"
