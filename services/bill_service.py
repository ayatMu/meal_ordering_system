from uuid import UUID
from models.bill import Bill
from utilities.base_service import BaseService
from utilities.db_utils import fetch_data
from utilities.db_utils import execute_query
from utilities.general_utils import generate_id
from datetime import datetime 


class BillService(BaseService):
    def rows_to_dict(self, rows):
        return [dict(row) for row in rows]

    def list_all(self):
        # TODO: Implement this method
        query = "SELECT * FROM bills "
        rows = fetch_data(query)
        return self.rows_to_dict(rows) 

    def get_by_id(self, bill_id: UUID):
        query = "SELECT * FROM bills WHERE bill_id = ?"
        rows = fetch_data(query, (str(bill_id),))
        return self.rows_to_dict(rows)[0] if rows else None


    def add(self, bill: Bill):
        # TODO: Implement this method
        bill.id=generate_id()
        bill.payment_date = bill.payment_date if bill.payment_date is not None else datetime.now().strftime('%Y-%m-%d')

        bill.is_paid = False
        # bill.payment_date = datetime.now().strftime('%Y-%m-%d')
    
        query = """
        INSERT INTO bills (bill_id, user_id, total_amount,date,is_paid,payment_date)
        VALUES (?,?,?,?,?,?)
        """
        bill_data = (str(bill.id), bill.user_id, bill.total_amount,bill.date,bill.is_paid,bill.payment_date)
        execute_query(query, bill_data)
        print(f"Bill {bill.id} added successfully.")
        return f"Bill {bill.id} added successfully."


    def remove(self, bill_id: UUID):
        # TODO: Implement this method
        query = "DELETE FROM bills WHERE bill_id = ?"
        execute_query(query, (str(bill_id),))
        print(f"Bill {bill_id} removed successfully.")
        return f"Bill {bill_id} removed successfully."


    def update(self, bill_id: UUID, updated_info: dict):
        # TODO: Implement this method

        if not updated_info:
            raise ValueError("No fields to update")

        set_clause = ", ".join([f"{key} = ?" for key in updated_info.keys()])
        query = f"UPDATE bills SET {set_clause} WHERE bill_id = ?"

        
        params = list(updated_info.values()) + [str(bill_id)]
        
        execute_query(query, params)
        print(f"Bill {bill_id} updated successfully.")
        return f"Bill {bill_id} updated successfully."


