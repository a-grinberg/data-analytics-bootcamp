-- -- Part I
-- -- Create a table named purchases. It should have 3 columns :
-- -- id : the primary key of the table
-- -- customer_id : this column references the table customers
-- -- item_id : this column references the table items
-- -- quantity_purchased : this column is the quantity of items purchased by a certain customer

-- CREATE TABLE purchases (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_id INT NOT NULL,
-- 	item_id INT NOT NULL,
-- 	quantity_purchased INT NOT NULL,
-- 	FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
-- 	FOREIGN KEY (item_id) REFERENCES items(item_id)
-- );

-- -- Insert purchases for the customers, use subqueries:
-- -- Scott Scott bought one fan
-- -- Melanie Johnson bought ten large desks
-- -- Greg Jones bougth two small desks
-- INSERT INTO purchases (customer_id, item_id, quantity_purchased)
-- VALUES
-- 	(3,3,1),
-- 	(5,2,10),
-- 	(1,1,2);

-- Part II
-- Use SQL to get the following from the database:
--1. All purchases. Is this information useful to us?
SELECT *
FROM purchases;
-- not useful, just a bunch of ids

--2.All purchases, joining with the customers table.
SELECT *
FROM purchases AS p
JOIN customers AS c ON p.customer_id = c.customer_id;

--3. Purchases of the customer with the ID equal to 5.
SELECT p.id, i.item_name
FROM purchases AS p
JOIN items AS i ON p.item_id = i.item_id
WHERE p.customer_id = 5;

--4. Purchases for a large desk AND a small desk
SELECT p.id, i.item_name
FROM purchases AS p
JOIN items AS i ON p.item_id = i.item_id
WHERE p.item_id IN (2,1);
-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name
SELECT c.first_name, c.last_name, item_name
FROM purchases AS p
JOIN customers AS c ON p.customer_id = c.customer_id
JOIN items AS i ON p.item_id = i.item_id;
-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?



