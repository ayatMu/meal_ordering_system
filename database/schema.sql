--TODO: wirte the schema for the database by creating the tables and the relationships between them

CREATE TABLE IF NOT EXISTS bills(
bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
total_amount BOOLEAN,
FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS meals(
meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
name_meal TEXT,
price INTEGER
);
CREATE TABLE IF NOT EXISTS orders(
order_id INTEGER PRIMARY KEY AUTOINCREMENT,
bill_id INTEGER,
meal_id INTEGER, 
quantity INTEGER,
price FLOAT,
FOREIGN KEY (bill_id) REFERENCES bills(id)
FOREIGN KEY(meal_id) REFERENCES meals(id)
);
CREATE TABLE IF NOT EXISTS users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT, 
last_name TEXT,
age INTEGER,
user_name TEXT,
password INTEGER,
role TEXT
)



