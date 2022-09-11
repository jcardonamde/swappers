from app.config.mysqlconnection import connectToMySQL
import re
from flask import flash, session

class Service:

    def __init__(self, data):
        self.name = data['name']
        self.type_service = data['type_service']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.nickname = data['nickname']



    @classmethod
    def save_service(cls, formulario):#metodo de clase para insertar un servicio en la base de datos con todos los datos sin excepción(name, type_service, description, user_id) y regresara id del servicio
        query = "INSERT INTO services(name, type_service, description, user_id) VALUES ('%(name)s', '%(type_service)s', '%(description)s', '%(user_id)s');"
        result = connectToMySQL('swappers').query_db(query, formulario) 
        return result 

    @staticmethod
    def validate_service(formulario):
        es_valido=True

        if len(formulario['name']) < 3:
            flash('The service must have a name of at least 3 characters', 'add_service')#esta categoria debe ser puesta en el HTML donde se encuentra la creación de servicios
            es_valido=False

        if formulario['type_Service'] == "":
            flash('You must select what type of service (category) you want to offer', 'add_service')#esta categoria debe ser puesta en el HTML donde se encuentra la creación de servicios
            es_valido=False

        if len(formulario['description']) < 5:
            flash('The service must have a description of at least 5 characters', 'add_service')#esta categoria debe ser puesta en el HTML donde se encuentra la creación de servicios
            es_valido=False

        return es_valido

    @classmethod
    def get_by_id(cls, formulario):#metodo de clase que obtiene todos los servicios de una determinada persona, su nombre, apellido y apodo, enviandole en el formulario el id de esa persona 
        query = "select services.*, users.first_name, users.last_name, users.nickname from services left join users on users.id = services.user_id where user_id=%(id)s;"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        services = []
        for service in result:
            services.append(cls(service))
        return services #regresa una lista con cada uno de los servicios hechos instancias que posee dicho usuario 
        

    @classmethod
    def delete_service(cls, formulario): #metodo de clase que sirve para borrar un servicio, al cual debe enviarsele el id del servicio
        query= "Delete from services where id=%(id)s;"
        result = connectToMySQL('swappers').query_db(query, formulario)
        return result

    @classmethod 
    def update_service(cls, formulario): #metodo de clase que sirve para actualizar un servicio, al cual debe enviarsele el id del servicio
        query= "update services set name=%(name)s, type_service=%(type_service)s, description=%(description)s where id=%(id)s"
        result = connectToMySQL('swappers').query_db(query, formulario)
        return result

    @classmethod
    def filter_services_by_city(cls, formulario):#metodo de clase que obtiene todos los servicios de una determinada ciudad,  nombre, apellido y apodo de la persona poseedora del servicio, enviandole en el formulario la city que se necesita 
        query = "select services.*, users.first_name, users.last_name, users.nickname from services left join users on users.id = services.user_id where city=%(city)s;"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        services = []
        for service in result:
            services.append(cls(service))
        return services #regresa una lista con cada uno de los servicios hechos instancias que posee dicho usuario 

    @classmethod
    def filter_services_by_type_services(cls, formulario):#metodo de clase que obtiene todos los servicios de una determinada categoria,  nombre, apellido y apodo de la persona poseedora del servicio, enviandole en el formulario la categoría que se necesita 
        query = "select services.*, users.first_name, users.last_name, users.nickname from services left join users on users.id = services.user_id where type_service=%(type_service)s;"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        services = []
        for service in result:
            services.append(cls(service))
        return services #regresa una lista con cada uno de los servicios hechos instancias que posee dicho usuario 

    @classmethod
    def pre_match(cls, formulario):#metodo de clase para hacer match con el servicio de una persona, necesita enviarse el servicio que se quiere y el id del usuario que lo quiere
        query = "INSERT INTO users_want_services (service_id, user_id) VALUES ('%(service_id)s', '%(user_id)s');"
        result = connectToMySQL('swappers').query_db(query, formulario) 
        return result 

