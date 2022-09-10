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
    def get_by_id(cls, formulario):#metodo de clase que obtiene todos los servicios de una determinada persona, enviandole en el formulario el id de esa persona 
        query = "select * from services where user_id=%(id)s;"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        services = []
        for service in result:
            services.append(cls(service))
        return services #regresa una lista con cada uno de los servicios hechos instancias que posee dicho usuario 
        

"""    @classmethod
    def delete(cls, formulario): #delete
        query= "Delete from appointments where id=%(id)s;"
        result = connectToMySQL('swappers').query_db(query, formulario)
        return result

    @classmethod 
    def update(cls, formulario): #

        query= "update appointments set task=%(task)s, date=%(date)s, status=%(status)s where id=%(id)s"
        result = connectToMySQL('swappers').query_db(query, formulario)
        return result

    @classmethod
    def get_info(cls, formulario):
        query = "select * from appointments where id=%(id)s;"
        result = connectToMySQL('swappers').query_db(query, formulario) #Select recibe lista
        return cls(result[0])"""

#query para filtrar servicios por ciudad
#query para filtrar servicios por categoria 
