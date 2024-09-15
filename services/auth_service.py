from models.user import User
from services import user_service
from services.user_service import  UserService
from utilities.db_utils import execute_query
from utilities.general_utils import generate_id


from utilities.general_utils import verify_password, hash_password


class AuthenticationService:
    def __init__(self, db_connection):
        self.current_user = None
        self.db_connection = db_connection
        self.user_service = UserService(self.db_connection)


    def signin(self, username: str, password: str):
        # TODO: Implement this method
        user = UserService.get_by_id(self.db_connection, username)
        if not user:
            return "User not found"
        if not verify_password(password, user.password_hash):
            return "Invalid password"
        self.current_user = user
        return "Signed in successfully"


    def signup(self, first_name: str, last_name: str, age: int, user_name: str, password: str,):
        # TODO: Implement this method
        # if UserService.get_by_id(id):
        #     return "Username already taken"
        user_id=generate_id()
        password_hash = hash_password(password)
        # first_name=first_name,
        # last_name=last_name,
        # age=age,
        # user_name=user_name,
        # password_hash=password_hash,
    
        query= " INSERT INTO users (user_id,first_name,last_name,age,user_name,password,role) VALUES (%s,%s ,%s ,%s ,%s ,%s ,user) "
        result= (user_id,first_name,last_name,age,user_name, password_hash)
        execute_query (query, result)
        print(execute_query)
        return "Signup successful"
        

    def signout(self, user_id: str):
        # TODO: Implement this method
        pass
