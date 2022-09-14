from crypt import methods
from flask import render_template, redirect, session, request, flash
from app import app
from app.models.users import User
from app.models.services import Service
from app.models.match import match




# Template para crear servicios 
@app.route('/create_services')
def create_services():
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        "id": session['user_id']
    }
    
    user = User.get_by_id(formulario)
    return render_template('create_service.html', user=user)



# Guardar los servicios en la DB
@app.route('/add_service', methods=['POST'])
def create_service():

    if not Service.validate_service(request.form):
        return redirect('/create_services')
    else:
        Service.save_service(request.form)
        return redirect('/dashboard')


# Ruta para hacer el match
@app.route('/match_service/<int:service_id>/<int:user_id>')
def match_service(service_id, user_id):
    formulario = {
        "service_id": service_id,
        "user_id" : user_id
    }
    match.pre_match(formulario)
    return redirect('/dashboard')


# Template edit service
@app.route('/edit/sevice/<int:service_id>') 
def edit_service(service_id):
    if 'user_id' not in session: 
        return redirect('/')
    
    formulario = {
        "id": session['user_id']
    }

    user = User.get_by_id(formulario)
    formulario_service = { "service_id": service_id }

    services = Service.get_by_id(formulario_service)

    return render_template('edit.html', user=user, services=services)

#Edit services
@app.route('/edit_service', methods=['POST'])
def edit_service():
    formulario ={
        "name" : request.form["name"],
        "type_service" : request.form["type_service"],
        "description" : request.form["description"],
        "id" : request.form["id"]
    }
    Service.update_service(formulario)
    return redirect('/dashboard')


# Delete service
@app.route('/delete_service/<int:service_id>')
def delete_service(service_id):
    formulario = {
        "service_id": service_id,
    }
    Service.delete_service(formulario)
    return redirect('/dashboard')


# Delete match
@app.route('/delete_match/<int:service_id>/<int:user_id>')
def delete_match(service_id, user_id):
    formulario = {
        "service_id": service_id,
        "user_id" : user_id
    }
    match.delete_pre_match(formulario)
    return redirect('/dashboard')

