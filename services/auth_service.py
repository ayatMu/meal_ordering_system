from models.user import User
from services import user_service
from services.user_service import  UserService
from utilities.db_utils import execute_query
from utilities.general_utils import generate_id
from uuid import UUID


from utilities.general_utils import verify_password, hash_password


class AuthenticationService:
    def __init__(self, db_connection):
        self.current_user = None
        self.db_connection = db_connection
        self.user_service = UserService(self.db_connection)


    def signin(self, user_name: str, password: str):
        # TODO: Implement this method
        user = self.user_service.get_by_username(user_name)
        if user:
            stored_password = user['password']
            if verify_password(password, stored_password):
                self.current_user = user 
                self.user_service.update_login_status(user['user_id'], True)
                return f"User {user_name} signed in successfully."
        return "Invalid username or password."

    def signup(self,first_name: str, last_name: str, age: int, user_name: str, password: str):
        new_user = {
            'user_id':generate_id(),
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'username': user_name,
            'password': password,
            'role': 'user',
            'is_loggedin': False
        }
        return self.user_service.add(new_user)

    def signout(self, user_id: str):
        self.user_service.update_login_status(user_id, False)
        self.current_user = None
        return f"User with ID {user_id} signed out successfully."
        

    def signout(self, user_id: str):
        # TODO: Implement this method
        self.user_service.update_login_status(user_id, False)
        self.current_user = None
        print(f"User with ID {user_id} signed out success")
        return f"User with ID {user_id} signed out success"