--1--
SELECT COUNT(actor_id)
FROM actors;

--2--
INSERT INTO actors (first_name, last_name, birthdate, number_oscars)
VALUES ('Tom', 'Holland', '01/06/1996')

-- ERROR:  INSERT has more target columns than expressions --