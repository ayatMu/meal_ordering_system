from uuid import UUID
from models.user import User
from utilities.base_service import BaseService
from utilities.db_utils import execute_query
import sqlite3
from abc import ABC, abstractmethod

class UserService(BaseService):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def list_all(self,get_db_connection):
        # TODO: Implement this method
        # get_db_connection.execute('select *')
        pass
    

    def get_by_id(self, user_name):
        # تغيير اسم العمود إلى username
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user_name,))
        user = cursor.fetchone()  # الحصول على أول نتيجة
        cursor.close()
        return user

    def add(self,first_name,last_name,age,user_name,password ):
        # TODO: Implement this method\
        query= " INSERT INTO users (first_name,last_name,age,user_name,password ) VALUES (%s ,%s ,%s ,%s ,%s ,) "
        result= (first_name,last_name,age,user_name,password)
        execute_query (query, result)
        


    def remove(self, user_id: UUID):
        # TODO: Implement this method
        pass

    def update(self, user_id: UUID, updated_info: dict):
        # TODO: Implement this method
        pass
