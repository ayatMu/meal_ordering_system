from abc import ABC, abstractmethod
import sqlite3

class BaseService(ABC):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    @abstractmethod
    def list_all(self):
        pass
        # cursor = self.db_connection.cursor()
        # query = "SELECT * FROM entities" 
        # cursor.execute(query)
        # results = cursor.fetchall()
        # cursor.close()
        # return results


    @abstractmethod
    def get_by_id(self, entity_id):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM entities WHERE id = ?"
        cursor.execute(query, (entity_id,))
        result = cursor.fetchone()
        cursor.close()
        return result


    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def remove(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity_id, updated_info):
        pass
