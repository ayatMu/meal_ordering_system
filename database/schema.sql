--TODO: wirte the schema for the database by creating the tables and the relationships between them

CREATE TABLE IF NOT EXISTS bills(
bill_id UUID PRIMARY KEY,
user_id UUID,
total_amount BOOLEAN,
date DATETIME,
is_paid BOOLEAN,
payment_date DATETIME,
FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS meals(
meal_id UUID PRIMARY KEY,
name_meal TEXT,
price INTEGER
);

CREATE TABLE IF NOT EXISTS orders(
order_id UUID PRIMARY KEY,
bill_id UUID,
meal_id UUID, 
quantity INTEGER,
price FLOAT,
FOREIGN KEY (bill_id) REFERENCES bills(id)
FOREIGN KEY(meal_id) REFERENCES meals(id)
);


CREATE TABLE IF NOT EXISTS users(
user_id UUID PRIMARY KEY,
first_name TEXT, 
last_name TEXT,
age INTEGER,
user_name TEXT,
password TEXT,
role TEXT,
is_loggedin BOOLEAN
)



