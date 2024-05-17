CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL
);

INSERT INTO students (first_name, last_name, birth_date)
VALUES
	('Marc', 'Benichou', '02/11/1998'),
	('Yoan', 'Cohen', '03/12/2010'),
	('Lea',	'Benichou', '27/07/1987'),
	('Amelia', 'Dux', '07/04/1996'),
	('David', 'Grez', '14/06/2003'),
	('Omer', 'Simpson', '03/10/1980'),
	('Artem', 'Grinberg', '17/10/1988');
--1--
SELECT *
FROM students;

--2--
SELECT first_name, last_name
FROM students;

--3.1--
SELECT first_name, last_name
FROM students
WHERE id=2;

--3.2--
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

--3.3--
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

--3.4--
SELECT first_name, last_name
FROM students
WHERE first_name LIKE '%a%';

--3.5--
SELECT first_name, last_name
FROM students
WHERE first_name LIKE 'a%';
	
--3.6--
SELECT first_name, last_name
FROM students
WHERE first_name LIKE '%a';
	
--3.7--
SELECT first_name, last_name
FROM students
WHERE first_name LIKE '%a';

--3.8--
SELECT first_name, last_name
FROM students
WHERE POSITION('a' in first_name) = LENGTH(first_name)-1;

--4--
SELECT *
FROM students
WHERE birth_date >= '1/01/2000';