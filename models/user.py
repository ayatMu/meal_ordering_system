from utilities.general_utils import generate_id
class User:
    def __init__(
        self, first_name, last_name, age, username, password, role, id=generate_id()) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.password = password
        self.is_loggedin = False
        self.role = role
