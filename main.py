from database.db_connection import get_db_connection
from models.user import User
from models.meal import Meal
from models.bill import Bill
from models.order import Order
from services.auth_service import AuthenticationService
from services.user_service import UserService
from services.meal_service import MealService
from services.bill_service import BillService
from services.order_service import OrderService
from utilities.general_utils import generate_id

def display_menu(options):
    print("\nMenu:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Choose an option: "))
    return choice

def handle_admin_menu(auth_service, user_service, meal_service, bill_service, order_service):
    options = ["List Users", "Add User", "Remove User", "Update User",
               "List Meals", "Add Meal", "Remove Meal", "Update Meal",
               "List Bills", "List Orders", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(user_service.list_all())
    elif choice == 2:
        username = input("Username: ")
        password = input("Password: ")
        age = int(input("Age: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        user = User(username=username, password=password, age=age, first_name=first_name, last_name=last_name)
        user_service.add(user)
    elif choice == 3:
        user_id = input("User ID to remove: ")
        user_service.remove(user_id)
    elif choice == 4:
        user_id = input("User ID to update: ")
        updated_info = {
            "username": input("New Username: "),
            "age": int(input("New Age: ")),
            "first_name": input("New First Name: "),
            "last_name": input("New Last Name: "),
            "role": input("New Role (admin/cashier/user): ")
        }
        user_service.update(user_id, updated_info)
    elif choice == 5:
        print(meal_service.list_all())
    elif choice == 6:
        name = input("Meal Name: ")
        price = float(input("Price: "))
        meal = Meal(name=name, price=price)
        meal_service.add(meal)
    elif choice == 7:
        meal_id = input("Meal ID to remove: ")
        meal_service.remove(meal_id)
    elif choice == 8:
        meal_id = input("Meal ID to update: ")
        updated_info = {
            "name": input("New Meal Name: "),
            "price": float(input("New Price: "))
        }
        meal_service.update(meal_id, updated_info)
    elif choice == 9:
        print(bill_service.list_all())
    elif choice == 10:
        print(order_service.list_all())
    elif choice == 11:
        return auth_service.signout(auth_service.current_user['id'])
    else:
        print("Invalid choice")

def handle_cashier_menu(bill_service):
    options = ["List Bills", "Mark Bill as Paid", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(bill_service.list_all())
    elif choice == 2:
        bill_id = input("Bill ID to mark as paid: ")
        bill_service.update(bill_id)
    elif choice == 3:
        return auth_service.signout(auth_service.current_user['id'])
    else:
        print("Invalid choice")

def handle_user_menu(meal_service, bill_service, order_service):
    options = ["List Meals", "Order Meals", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(meal_service.list_all())
    elif choice == 2:
        user_id = auth_service.current_user['id']
        bill_id = generate_id()
        orders = []
        while True:
            meal_id = input("Meal ID to order (0 to finish): ")
            if meal_id == "0":
                break
            meal = meal_service.get_by_id(meal_id)
            if not meal:
                print("Meal not found")
                continue
            quantity = int(input("Quantity: "))
            order = Order(bill_id, meal_id, quantity, meal.price)
            orders.append(order)
        bill = Bill(user_id, sum(order.total_price * quantity for order in orders), bill_id)
        bill_service.add(bill)
        for order in orders:
            order_service.add(order)       
    elif choice == 3:
        return auth_service.signout(auth_service.current_user['id'])
    else:
        print("Invalid choice")

def main():
    db_conn = get_db_connection()

    global auth_service
    auth_service = AuthenticationService(db_conn)
    user_service = UserService(db_conn)
    meal_service = MealService(db_conn)
    bill_service = BillService(db_conn)
    order_service = OrderService(db_conn)

    while True:
        if auth_service.current_user:
            role = auth_service.current_user['role']
            if role == "admin":
                handle_admin_menu(auth_service, user_service, meal_service, bill_service, order_service)
            elif role == "cashier":
                handle_cashier_menu(bill_service)
            elif role == "user":
                handle_user_menu(meal_service, bill_service, order_service)
        else:
            options = ["Sign In", "Sign Up", "Exit"]
            choice = display_menu(options)

            if choice == 1:
                username = input("Username: ")
                password = input("Password: ")
                auth_service.signin(username, password)
            elif choice == 2:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = input("Username: ")
                password = input("Password: ")
                age = int(input("Age: "))
                print(auth_service.signup(first_name, last_name, age, username, password))
            elif choice == 3:
                print("Exiting...")
                break

if __name__ == "__main__":
    main()
