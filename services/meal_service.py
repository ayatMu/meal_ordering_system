from uuid import UUID
from models.meal import Meal
from utilities.base_service import BaseService


class MealService(BaseService):
    def list_all(self):
        # TODO: Implement this method
        pass

    def get_by_id(self, meal_id: UUID):
        pass

    def add(self, meal: Meal):
        # TODO: Implement this method
        pass

    def remove(self, meal_id: UUID):
        # TODO: Implement this method
        pass

    def update(self, meal_id: UUID, updated_info: dict):
        # TODO: Implement this method
        pass
