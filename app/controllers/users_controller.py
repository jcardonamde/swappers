from flask import render_template, redirect, session, request, flash
from app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

# Template preview
@app.route('/')
def index():
    return render_template('index.html')


# Template Login
@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('login.html')


# Template Registro
@app.route('/registro')
def registro():
    return render_template('register.html')


# Template Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('dashboard.html')



#Ruta para iniciar sesion y redirigirse al dashboard
@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Email o Contraseña incorrectos", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Email o Contraseña incorrectos", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')



#Ruta para registrarse y redirigirse al dashboard
@app.route('/register', methods=['POST'])
def register():

    if not User.valida_usuario(request.form):
        return redirect('/registro')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash 
    }
    
    
    id = User.save(data)

    session['user_id'] = id
    return redirect('/dashboard')