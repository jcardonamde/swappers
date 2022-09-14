print("Hola mundo")
from flask import render_template,redirect,session,request,flash #importaciones de modulos de flask
from app import app

#Importando el Bcript
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt(app)#inicializando instancia bcrypt

@app.route('/')
def main():
    return render_template('dashboard.html')