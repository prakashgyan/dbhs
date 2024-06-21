from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/create_sign')
@login_required
def create_sign():
    return render_template('create_sign.html')

@main.route('/display/<uuid>')
def display_sign(uuid):
    # Fetch sign data based on UUID
    return render_template('display_sign.html', sign=sign)