from uuid import UUID
from models.order import Order
from utilities.base_service import BaseService
from utilities.db_utils import fetch_data
from uuid import uuid4
from utilities.db_utils import execute_query
class OrderService(BaseService):


    def rows_to_dict(self, rows):
        return [dict(row) for row in rows]

    def list_all(self):
        # TODO: Implement this method
        query = "SELECT * FROM orders "
        rows = fetch_data(query)
        return self.rows_to_dict(rows) 

    def get_by_id(self, order_id: UUID):
        query = "SELECT * FROM orders WHERE order_id = ?"
        rows = fetch_data(query, (str(order_id),))
        return self.rows_to_dict(rows)[0] if rows else None


    def add(self, order: Order):
        # TODO: Implement this method
        query = """
        INSERT INTO orders (order_id, bill_id, meal_id, quantity,price)
        VALUES (?, ?, ?, ?, ?)
        """
        order_id = str(uuid4())
        order_data = (
            order_id, order.bill_id, order.meal_id, order.quantity,
            order.price
        )
        execute_query(query, order_data)
        print(f"Order {order_id} added successfully.")
        return f"Order {order_id} added successfully."


    def remove(self, order_id: UUID):
        # TODO: Implement this method
        query = "DELETE FROM orders WHERE order_id = ?"
        execute_query(query, (str(order_id),))
        print(f"Order {order_id} removed successfully.")
        return f"Order {order_id} removed successfully."


    def update(self, order_id: UUID, updated_info: dict):
        # TODO: Implement this method
        
        query = """
        UPDATE orders 
        SET bill_id = ?, meal_id = ?, quantity = ?, price = ? 
        WHERE order_id = ?
        """
        order_data = (
            updated_info.get('bill_id'),
            updated_info.get('meal_id'),
            updated_info.get('quantity'),
            updated_info.get('price'),
            str(order_id)
        )
        execute_query(query, order_data)
        print(f"Order {order_id} updated successfully.")
        return f"Order {order_id} updated successfully."

