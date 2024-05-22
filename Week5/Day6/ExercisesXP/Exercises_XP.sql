-- Exercise 1: DVD Rental
-- Instructions
--1. Get a list of all the languages, from the language table.
SELECT *
FROM language;

--2. Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT f.title, f.description,l.name
FROM film AS f
JOIN language AS l ON f.language_id = l.language_id;

--3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
SELECT f.title, f.description,l.name
FROM film AS f
FULL OUTER JOIN language AS l ON f.language_id = l.language_id;
--4. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film (
	film_id SERIAL PRIMARY KEY,
	film_name VARCHAR NOT NULL
);
INSERT INTO new_film (film_name)
VALUES
	('Kingdom of the Planet of the Apes'),
	('The Ministry of Ungentlemanly Warfare'),
	('Furiosa: A Mad Max Saga'),
	('Megalopolis'),
	('The Idea of You'),
	('Mother of the Bride'),
	('Challengers');
--5. Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
	--1. review_id – a primary key, non null, auto-increment.
	--2. film_id – references the new_film table. The film that is being reviewed.
	--3. language_id – references the language table. What language the review is in.
	--4. title – the title of the review.
	--5. score – the rating of the review (1-10).
	--6. review_text – the text of the review. No limit on the length.
	--7. last_update – when the review was last updated.
CREATE TABLE customer_review (
	review_id SERIAL PRIMARY KEY,
	film_id INT NOT NULL,
	language_id INT NOT NULL,
	title VARCHAR(100) NOT NULL,
	score INT NOT NULL,
	review_text TEXT NOT NULL,
	last_update TIMESTAMP,
	FOREIGN KEY (film_id) REFERENCES new_film(film_id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE NO ACTION
);

--6 Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
	(3, 1, 'Excellent', 5, 'Good plot, wonderfull perfomace of actors'),
	(5, 1, 'Not bad', 4, 'Kinda film, wich attracted me');

--7 Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film
WHERE film_id = 3;
-- film's review was deleted as well

-- Exercise 2 : DVD Rental
-- Instructions
--1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 3
WHERE film_id IN (2, 5, 7, 35, 49);
--2. Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

--3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE customer_review -- we can just drop this table, because there are no any critical dependencies in other tables

--4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(rental_id)
FROM rental
WHERE return_date IS NULL
--5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.title
FROM film as f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL
ORDER BY rental_rate
LIMIT 30
--6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
	--1 The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT *
FROM film AS f
JOIN film_actor AS fa ON f.film_id = fa.film_id
JOIN actor AS a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo wrestler%' AND CONCAT(a.first_name, ' ', a.last_name) = 'Penelope Monroe'	
	--2 The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT *
FROM film
WHERE rating = 'R' AND length/60 < 1;	
	--3 The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.title
FROM film as f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
JOIN customer AS c ON r.customer_id = c.customer_id
JOIN payment AS p ON c.customer_id = p.customer_id
WHERE CONCAT(c.first_name, ' ', c.last_name) = 'Matthew Mahan' AND p.amount > 4.0 AND (r.return_date > '2005-07-28' AND r.return_date < '2005-08-01')
GROUP BY f.title	
	--4 The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT f.title
FROM film as f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
JOIN customer AS c ON r.customer_id = c.customer_id
WHERE CONCAT(c.first_name, ' ', c.last_name) = 'Matthew Mahan' AND (f.description ILIKE '%boat%' or f.title ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1