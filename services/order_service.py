from uuid import UUID
from models.order import Order
from utilities.base_service import BaseService


class OrderService(BaseService):
    def list_all(self):
        # TODO: Implement this method
        pass

    def get_by_id(self, order_id: UUID):
        pass

    def add(self, order: Order):
        # TODO: Implement this method
        pass

    def remove(self, order_id: UUID):
        # TODO: Implement this method
        pass

    def update(self, order_id: UUID, updated_info: dict):
        # TODO: Implement this method
        pass
