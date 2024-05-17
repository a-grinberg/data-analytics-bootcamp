--1--
SELECT *
FROM students
ORDER BY
	last_name ASC
LIMIT 4;

--2--
SELECT *
FROM students
ORDER BY
	birth_date DESC
LIMIT 1;

--3--
SELECT *
FROM students
LIMIT 3
OFFSET 2