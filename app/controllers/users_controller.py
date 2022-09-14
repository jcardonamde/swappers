from crypt import methods
from flask import render_template, redirect, session, request, flash, jsonify
from app import app
from app.models.users import User
from app.models.services import Service
from app.models.match import match


from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
from werkzeug.utils import secure_filename
import os

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



@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404 #status200

# Template Dashboard
@app.route('/dashboard', methods=['POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    formulario = {
        "id": session['user_id']
    }
    city = { "city" : request.form["city"] }
    type_service = { "type_service" : request.form["type_service"] }
    all_services = Service.get_all()
    filter_city = Service.filter_services_by_city(city)
    filter_type = Service.filter_services_by_type_services(type_service)
    user = User.get_by_id(formulario)
    matches= match.match(formulario)
    return render_template('dashboard.html', user=user, all_services=all_services, filter_city=filter_city, filter_type=filter_type, matches= matches)



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

    
    image = request.files['image']
    nombre_imagen = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_imagen)) #guardar la imagen

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash ,
        "city": request.form['city'],
        "nickname": request.form['nickname'],
        "image": nombre_imagen
    }
    
    id = User.save_user(data)

    session['user_id'] = id
    return redirect('/dashboard')


#Cerrar Sesion
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')