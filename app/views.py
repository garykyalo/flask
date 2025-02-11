from flask import Blueprint
import pandas 



views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return "welcome"