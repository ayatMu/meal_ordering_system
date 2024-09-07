from models.user import User
from services import user_service
from utilities.general_utils import verify_password, hash_password


class AuthenticationService:
    def __init__(self, db_connection):
        self.current_user = None
        self.db_connection = db_connection

    def signin(self, username: str, password: str):
        # TODO: Implement this method
        pass

    def signup(self, first_name: str, last_name: str, age: int, username: str, password: str):
        # TODO: Implement this method
        pass

    def signout(self, user_id: str):
        # TODO: Implement this method
        pass
