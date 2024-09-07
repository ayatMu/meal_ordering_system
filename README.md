## Task Description: Food Ordering System

### **Project Overview**

In this task, you will implement a food ordering system using object-oriented programming (OOP) principles, but instead of using text files (CSV), the system will now use an SQL database for data storage. The system will manage users, meals, orders, and bills, and include authentication functionality. You will work within the provided folder structure and implement SQL queries and database interactions.

### **File Structure**

1. **database Folder**
   - **db_connection.py**: Contains the method to establish and manage a database connection.
   - **schema.sql**: Contains the SQL schema for creating necessary tables (users, meals, bills, and orders).

2. **models Folder**
   - **bill.py**: Defines the `Bill` class structure.
   - **meal.py**: Defines the `Meal` class structure.
   - **user.py**: Defines the `User` class structure.
   - **order.py**: Defines the `Order` class structure, which now handles multiple meals in one order.

3. **services Folder**
   - **auth_service.py**: Handles authentication operations (sign-in, sign-up, sign-out, password hashing).
   - **bill_service.py**: Manages operations related to bills.
   - **meal_service.py**: Manages operations related to meals.
   - **user_service.py**: Manages operations related to users.
   - **order_service.py**: Manages operations related to orders.

4. **utilities Folder**
   - **base_service.py**: Provides a base class with common service methods.
   - **db_utils.py**: Contains functions to interact with the database (e.g., executing queries and fetching data).
   - **general_utils.py**: Contains utility functions like password hashing and ID generation.

5. **main.py**: The entry point of the application, managing user interactions and invoking methods from service classes.

### Project Structure:
The project should follow this folder structure:
- **`database/`**
  - `db_connection.py`: Manages the database connection.
  - `schema.sql`: Contains the SQL schema for setting up database tables.
  
- **`models/`**
  - `user.py`: Defines the `User` class.
  - `meal.py`: Defines the `Meal` class.
  - `bill.py`: Defines the `Bill` class.
  - `order.py`: Defines the `Order` class.
  
- **`services/`**
  - `auth_service.py`: Manages user authentication.
  - `user_service.py`: Manages user-related operations.
  - `meal_service.py`: Manages meal-related operations.
  - `bill_service.py`: Manages billing operations.
  - `order_service.py`: Manages order operations.
  
- **`utilities/`**
  - `db_utils.py`: Provides utility functions for interacting with the database.
  
- **`main.py`**: The main file that interacts with all components and manages user input.

### **Task Requirements**

1. **Implement Database Schema**:
   - **schema.sql**: Write SQL queries to create tables for `users`, `meals`, `bills`, and `orders` (where an order can contain multiple meals).
   - Ensure each table uses a `UUID` for unique identifiers.

2. **Database Connection**:
   - **db_connection.py**: Implement a method `get_db_connection()` to establish and return a connection to the database.

3. **Implement Service Methods**:
   - Refactor service methods to use SQL queries instead of text files:
     - **list_all**: Fetch and list all records for the corresponding entity (e.g., meals, users, bills).
     - **add**: Insert a new record into the database.
     - **remove**: Remove an existing record from the database.
     - **update**: Update an existing record in the database.

4. **DB Utilities**:
   - Implement utility functions in `db_utils.py`:
     - `fetch_data(query: str, params: tuple = ())`: Fetch data from the database using the provided query and parameters.
     - `execute_query(query: str, params: tuple = ())`: Execute a query (insert, update, delete) on the database using the provided query and parameters.

5. **Implement Order Management**:
   - Update the system to handle multiple meals in a single order.

6. **Authentication Methods**:
   - Implement the authentication methods (sign-in, sign-up, sign-out) using database records.

7. **Database Design**:

   - Use **Draw.io** to create an ERD that reflects the relationships between users, bills, and meals.
   - Set up your database schema in the DBMS of your choice.
   - Ensure proper table relationships for users, bills, orders and meals.
   - Include the ERD diagram in the project folder.

#### **Hints**

- **Database**: You can choose any DBMS (MySQL, PostgreSQL, SQLite, etc.) for your implementation.
- **UUIDs**: Use Python’s `uuid` module to generate unique IDs for the records.
- **Schema**: Ensure the schema is designed to handle relationships, such as multiple meals in one order.

#### **Deadline**

- The task is due one week from today, **September 13, 2024, 12:00 AM**.

#### **Bonus** (Optional)

- Add a **testing folder** and implement unit tests for the service classes, testing CRUD operations and edge cases.

#### **Submission**

- Submit your completed project by pushing it to a new branch in the same repository as your previous task with depending on the flow that we discussed before. Ensure that all files are included and that the project runs without errors.
