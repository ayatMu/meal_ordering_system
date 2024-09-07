### Functions Descriptions:

#### 1. `database/db_connection.py`
- **Function**: `connect_to_db()`
  - **Input**: None
  - **Output**: A connection object to the database
  - **Usage**: Establishes a connection to the SQLite database to be used by the services.

#### 2. `models/user.py`
- **Class**: `User`
  - **Attributes**: `id`, `first_name`, `last_name`, `username`, `password`, `role`, `is_loggedin`
  - **Input**: User information (e.g., first name, last name, username, etc.)
  - **Output**: A `User` object
  - **Usage**: Represents a user in the system, used for user-related operations.

#### 3. `models/meal.py`
- **Class**: `Meal`
  - **Attributes**: `id`, `name`, `price`
  - **Input**: Meal information (e.g., name, price)
  - **Output**: A `Meal` object
  - **Usage**: Represents a meal in the system, used for managing meals.

#### 4. `models/bill.py`
- **Class**: `Bill`
  - **Attributes**: `id`, `user_id`, `total_price`, `status`
  - **Input**: Bill information (e.g., user ID, total price, status)
  - **Output**: A `Bill` object
  - **Usage**: Represents a bill in the system, used for managing bills and tracking payment.

#### 5. `models/order.py`
- **Class**: `Order`
  - **Attributes**: `id`, `bill_id`, `meal_id`, `quantity`
  - **Input**: Order information (e.g., bill ID, meal ID, quantity)
  - **Output**: An `Order` object
  - **Usage**: Represents an order (a meal in a bill) in the system.

#### 6. `services/auth_service.py`
- **Function**: `signin(username, password)`
  - **Input**: `username` (string), `password` (string)
  - **Output**: Boolean (`True` for success, `False` for failure)
  - **Usage**: Validates a user’s credentials during login.
  
- **Function**: `signup(first_name, last_name, username, password)`
  - **Input**: `first_name`, `last_name`, `username`, `password`
  - **Output**: Success or failure message
  - **Usage**: Registers a new user in the system.

- **Function**: `signout(user_id)`
  - **Input**: `user_id` (UUID)
  - **Output**: None
  - **Usage**: Logs the user out by updating their login status.

#### 7. `services/user_service.py`
- **Function**: `add(user)`
  - **Input**: A `User` object
  - **Output**: Success or failure message
  - **Usage**: Adds a new user to the database.

- **Function**: `list_all()`
  - **Input**: None
  - **Output**: List of all users
  - **Usage**: Fetches all registered users from the database.

- **Function**: `remove(user_id)`
  - **Input**: `user_id` (UUID)
  - **Output**: Success or failure message
  - **Usage**: Deletes a user by their ID.

- **Function**: `update(user_id, updated_info)`
  - **Input**: `user_id` (UUID), `updated_info` (dictionary with new values)
  - **Output**: Success or failure message
  - **Usage**: Updates user information in the database.

#### 8. `services/meal_service.py`
- **Function**: `add(meal)`
  - **Input**: A `Meal` object
  - **Output**: Success or failure message
  - **Usage**: Adds a new meal to the database.

- **Function**: `list_all()`
  - **Input**: None
  - **Output**: List of all meals
  - **Usage**: Fetches all available meals from the database.

- **Function**: `remove(meal_id)`
  - **Input**: `meal_id` (UUID)
  - **Output**: Success or failure message
  - **Usage**: Deletes a meal from the database.

- **Function**: `update(meal_id, updated_info)`
  - **Input**: `meal_id` (UUID), `updated_info` (dictionary with new values)
  - **Output**: Success or failure message
  - **Usage**: Updates meal information in the database.

#### 9. `services/bill_service.py`
- **Function**: `add(bill)`
  - **Input**: A `Bill` object
  - **Output**: Success or failure message
  - **Usage**: Adds a new bill to the database.

- **Function**: `list_all()`
  - **Input**: None
  - **Output**: List of all bills
  - **Usage**: Fetches all bills from the database.

- **Function**: `update(bill_id, status)`
  - **Input**: `bill_id` (UUID), `status` (string, e.g., "Paid")
  - **Output**: Success or failure message
  - **Usage**: Updates the status of a bill.

#### 10. `services/order_service.py`
- **Function**: `add(order)`
  - **Input**: An `Order` object
  - **Output**: Success or failure message
  - **Usage**: Adds an order (meal within a bill) to the database.

- **Function**: `list_all()`
  - **Input**: None
  - **Output**: List of all orders
  - **Usage**: Fetches all orders from the database.

#### 11. `utilities/db_utils.py`
- **Function**: `execute_query(query, params=None)`
  - **Input**: `query` (SQL string), `params` (optional, parameters for the query)
  - **Output**: Success or failure message
  - **Usage**: Executes SQL queries (e.g., insert, update, delete) with optional parameters.

- **Function**: `fetch_all(query, params=None)`
  - **Input**: `query` (SQL string), `params` (optional, parameters for the query)
  - **Output**: List of results from the query
  - **Usage**: Fetches all records from a query result.

#### 12. `main.py`
- **Function**: `display_menu(options)`
  - **Input**: `options` (list of menu options)
  - **Output**: User's choice (integer)
  - **Usage**: Displays a menu and gets the user's choice.

- **Function**: `handle_admin_menu()`
  - **Input**: `auth_service`, `user_service`, `meal_service`, `bill_service`
  - **Output**: None
  - **Usage**: Manages admin-specific tasks (list users, add meals, etc.).

- **Function**: `handle_cashier_menu()`
  - **Input**: `bill_service`
  - **Output**: None
  - **Usage**: Manages cashier-specific tasks (list and update bills).

- **Function**: `handle_user_menu()`
  - **Input**: `meal_service`, `bill_service`
  - **Output**: None
  - **Usage**: Manages user-specific tasks (list meals, order meals).

