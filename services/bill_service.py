from uuid import UUID
from models.bill import Bill
from utilities.base_service import BaseService


class BillService(BaseService):
    def list_all(self):
        # TODO: Implement this method
        pass

    def get_by_id(self, bill_id: UUID):
        pass

    def add(self, bill: Bill):
        # TODO: Implement this method
        pass

    def remove(self, bill_id: UUID):
        # TODO: Implement this method
        pass

    def update(self, bill_id: UUID, updated_info: dict):
        # TODO: Implement this method
        pass
