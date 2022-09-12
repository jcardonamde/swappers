from app.config.mysqlconnection import connectToMySQL
import re
from flask import flash, session

class match:

    def __init__(self, data):
        self.name = data['name']
        self.type_service = data['type_service']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name_owner = data['first_name_owner']
        self.last_name_owner = data['last_name_owner']
        self.nickname_owner = data['nickname_owner']
        self.id_wanter = data['id_wanter']
        self.first_name_wanter = data['first_name_wanter']
        self.last_name_wanter = data['last_name_wanter']


    @classmethod
    def pre_match(cls, formulario):#metodo de clase para hacer match con el servicio de una persona, necesita enviarse el servicio que se quiere y el id del usuario que lo quiere
        query = "INSERT INTO users_want_services (service_id, user_id) VALUES ('%(service_id)s', '%(user_id)s');"
        result = connectToMySQL('swappers').query_db(query, formulario) 
        return result 

    @classmethod
    def match(cls, user_id):#metodo de clase que permittira obtener los matches que tiene es usuraio, es decir, las personas que quieren sus servicios, aparecera la información del servicio, el nombre, apellido y apodo de quien lo quiere, necesita enviarse el user_id del que incia sesión
        query = "select services.*, users.first_name as first_name_owner, users.last_name as last_name_owner, users.nickname as nickname_owner, users_want_services.user_id as id_wanter from  users left join services on users.id = services.user_id left join users_want_services on services.id = users_want_services.service_id where services.user_id=%(user_id)s;"        
        results = connectToMySQL('swappers').query_db(query, user_id) 
        matches = []
        if results == ():
            return None
        else:
            for result in results:
                formulario= {
                    "id":result['id_wanter']
                }
                query2 = "SELECT first_name as first_name_wanter, last_name as last_name_wanter FROM users WHERE id = %(id)s;"
                resultstwo = connectToMySQL('swappers').query_db(query2, formulario) 
                superresults={
                    self.name = result['name']
                    self.type_service = result['type_service']
                    self.description = result['description']
                    self.created_at = result['created_at']
                    self.updated_at = result['updated_at']
                    self.user_id = result['user_id']
                    self.first_name_owner = result['first_name_owner']
                    self.last_name_owner = result['last_name_owner']
                    self.nickname_owner = result['nickname_owner']
                    self.id_wanter = result['id_wanter']
                    self.first_name_wanter = resultstwo[0]['first_name_wanter']
                    self.last_name_wanter = resultstwo[0]['last_name_wanter']
                }
                service = cls(superresults)
                matches.append(service)
            return matches

    @classmethod
    def delete_pre_match(cls, formulario): #metodo de clase que sirve para borrar un posiible match, al cual debe enviarsele el id del servicio y el id del usuario que lo quiere
        query= "Delete from users_want_services where service_id='%(service_id)s' and user_id='%(user_id)s';"
        result = connectToMySQL('swappers').query_db(query, formulario)
        return result