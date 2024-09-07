from abc import ABC, abstractmethod

class BaseService(ABC):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    @abstractmethod
    def list_all(self):
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def remove(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, updated_info):
        pass
