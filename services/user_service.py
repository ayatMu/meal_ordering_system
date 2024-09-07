from uuid import UUID
from models.user import User
from utilities.base_service import BaseService


class UserService(BaseService):
    def list_all(self):
        # TODO: Implement this method
        pass

    def get_by_id(self, user_id: UUID):
        pass

    def add(self, user: User):
        # TODO: Implement this method
        pass

    def remove(self, user_id: UUID):
        # TODO: Implement this method
        pass

    def update(self, user_id: UUID, updated_info: dict):
        # TODO: Implement this method
        pass
