-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.
SELECT rating, COUNT(film_ID)
FROM film
GROUP BY rating;
--2. Get a list of all the movies that have a rating of G or PG-13.
SELECT title, rating
FROM film
WHERE rating IN ('G', 'PG-13');
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT title, rating
FROM film
WHERE rating IN ('G', 'PG-13') AND length / 60 < 2 AND rental_rate < 3.00
ORDER BY title;
--3. Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
UPDATE customer
SET first_name = 'Artem', last_name = 'Grinberg'
WHERE customer_id = 7;
--4. Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address
SET address = 'Gdalyau 21', phone = '888888888'
WHERE address_id = (SELECT address_id
				    FROM customer
					WHERE customer_id = 7);