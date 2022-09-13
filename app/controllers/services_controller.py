from flask import render_template, redirect, session, request, flash
from app import app
from app.models.users import User


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
def create_quiz():
    if 'user_id' not in session:  
        return redirect('/')

    if not Service.valida_service(request.form):
        return redirect('/create_services')
    else:
        Service.save(request.form)
        return redirect('/dashboard')