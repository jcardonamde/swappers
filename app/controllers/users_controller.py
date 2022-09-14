from app import app
from flask import render_template, redirect, session, request, flash, jsonify

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404 #status200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')