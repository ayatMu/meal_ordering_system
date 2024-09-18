from uuid import UUID
from models.user import User
from utilities.base_service import BaseService
from utilities.db_utils import execute_query
import sqlite3
from abc import ABC, abstractmethod
from utilities.general_utils import hash_password
from uuid import uuid4
from utilities.db_utils import fetch_data


class UserService(BaseService):
    def rows_to_dict(self, rows):
        return [dict(row) for row in rows]

    def list_all(self):
        # TODO: Implement this method
        query = "SELECT * FROM users "
        rows = fetch_data(query)
        return self.rows_to_dict(rows) 
        
    

    def get_by_id(self, user_name):
        query = "SELECT * FROM users WHERE username = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(query, (user_name,))
        user = cursor.fetchone()  
        cursor.close()
        return user
    
    def get_by_username(self, user_name: str):
            query = "SELECT * FROM users WHERE user_name = ?;"
            result = fetch_data(query, (user_name,))
            return result[0] if result else None
    
    # def add(self, user: dict):
    #     query = """
    #     INSERT INTO users (user_id, first_name, last_name,age, user_name, password,role,is_loggedin)
    #     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    #     """
    #     user_id = str(uuid4())
    #     hashed_password = hash_password(user['password'])
    #     user_data = (
    #     user_id, user.first_name, user.last_name, user.age, user.username,
    #     hashed_password, user.role, user.is_loggedin
    #     )
    #     execute_query(query, user_data)
    #     print (f"User {user.username} added successfully."),
    #     return f"User {user.username} added successfully."
    
    def add(self, user: dict):
        query = """
        INSERT INTO users (user_id, first_name, last_name, age, user_name, password, role, is_loggedin)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        hashed_password = hash_password(user['password'])
        user_data = (
            user['user_id'],
            user['first_name'],
            user['last_name'],
            user['age'],
            user['username'],
            hashed_password,
            user['role'],
            user['is_loggedin']
        )
    
        execute_query(query, user_data)
        return f"User {user['username']} added successfully."


    def update_login_status(self, user_id: str, is_loggedin: bool):
            query = "UPDATE users SET is_loggedin = ? WHERE user_id = ?;"
            execute_query(query, (is_loggedin, user_id))
            return f"User with ID {user_id} login status updated."
            


    def remove(self, user_id: UUID):
        # TODO: Implement this method
        query = "DELETE FROM users WHERE user_id = ?;"
        execute_query(query, (str(user_id),))
        print("removed successfully.")
        return f"User with ID {user_id} removed successfully."


    def update(self, user_id: UUID, updated_info: dict):
        fields = []
        values = []
        for key, value in updated_info.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(str(user_id))
        query = f"UPDATE users SET {', '.join(fields)} WHERE user_id = ?;"
        execute_query(query, values)
        print(f"User with ID {user_id} updated successfully.")
        return f"User with ID {user_id} updated successfully."