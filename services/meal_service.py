from uuid import UUID
from models.meal import Meal
from utilities.base_service import BaseService
from utilities.db_utils import fetch_data
from uuid import uuid4
from utilities.db_utils import execute_query


class MealService(BaseService):
    def rows_to_dict(self, rows):
        return [dict(row) for row in rows]

    def list_all(self):
        # TODO: Implement this method
        query = "SELECT * FROM meals "
        rows = fetch_data(query)
        return self.rows_to_dict(rows) 

    def get_by_id(self, meal_id: UUID):
        query = "SELECT * FROM meals WHERE meal_id = ?"
        rows = fetch_data(query, (str(meal_id),))
        return self.rows_to_dict(rows)[0] if rows else None


    def add(self, meal: Meal):
        # TODO: Implement this method
        query = """
        INSERT INTO meals (meal_id,name_meal, price)
        VALUES (?, ?, ?)
        """
        meal_id = str(uuid4())  
        meal_data = (meal_id, meal.name_meal, meal.price)
        execute_query(query, meal_data)
        print(f"Meal {meal.name_meal} added successfully.")
        return f"Meal {meal.name_meal} added successfully."

    def remove(self, meal_id: UUID):
        # TODO: Implement this method
        query = "DELETE FROM meals WHERE meal_id = ?"
        execute_query(query, (str(meal_id),))
        print(f"Meal with ID {meal_id} removed successfully.")
        return f"Meal with ID {meal_id} removed successfully."


    def update(self, meal_id: UUID, updated_info: dict):
        # TODO: Implement this method
        set_clause = ", ".join(f"{key} = ?" for key in updated_info.keys())
        query = f"UPDATE meals SET {set_clause} WHERE meal_id = ?"
        execute_query(query, (*updated_info.values(), str(meal_id)))
        return f"Meal with ID {meal_id} updated successfully."

