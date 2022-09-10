from app.config.mysqlconnection import connectToMySQL
import re
from flask import flash, session

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PWD_REGEX=re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.nickname = data['nickname']
        self.email = data['email']
        self.city = data['city']
        self.password = data['password']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_user(cls, formulario):#metodo de clase para insertar un usuario en la base de datos con todos los datos sin excepción(first_name, last_name, nickname, email, city, password, image) y regresara id del usuario
        query = "INSERT INTO users(first_name, last_name, nickname, email, city, password, image) VALUES (%(first_name)s, %(last_name)s, %(nickname)s, %(email)s, %(city)s, %(password)s, %(image)s )"
        result = connectToMySQL('swappers').query_db(query, formulario)  
        return result 

    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        if len(formulario['first_name']) < 3:
            flash('Name must have at least 3 characters', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro 
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash('Last name must have at least 3 characters', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro
            es_valido = False
        
        if not EMAIL_REGEX.match(formulario['email']): 
            flash('Invalid email', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro
            es_valido = False

        if not PWD_REGEX.match(formulario['password']):
            flash('Password must have at least 8 characters, a special character, a number, an uppercase and a lowercase', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro
            es_valido = False

        
        if formulario['password'] != formulario['confirm_password']:
            flash('Passwords do not match', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro
            es_valido = False
        
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('swappers').query_db(query, formulario)
        if len(results) >= 1:
            flash('Previously registered email', 'register')#esta categoria debe ser puesta en el HTML donde se encuentra el regisro
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, formulario): #debe enviarse email en el fromulario y regresara toda la informacion para la instancia
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('swappers').query_db(query, formulario)
        if len(result) < 1:#si no existe el email dara return false/usar para el login 
            return False
        else:
            user = cls(result[0]) 
            return user

    @classmethod
    def get_by_id(cls, formulario):#debe enviarse id en el fromulario y regresara toda la informacion para la instancia
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        user = cls(result[0])
        return user