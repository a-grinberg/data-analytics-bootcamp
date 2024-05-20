-- Update
--1. ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students
SET birth_date = '02/11/1998'
WHERE first_name in ('Lea', 'Marc') AND last_name = 'Benichou';
--2. Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

-- Delete
--1. Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students WHERE first_name = 'Lea' AND last_name = 'Benichou';

-- Count
--1. Count how many students are in the table.
SELECT COUNT(id)
FROM students;
-- Count how many students were born after 1/01/2000.
SELECT COUNT(id)
FROM students
WHERE birth_date < '01/02/2000';

-- Insert / Alter
-- 1. Add a column to the student table called math_grade.
ALTER TABLE students
ADD math_grade INT;
-- 2. Add 80 to the student which id is 1.
UPDATE students
SET math_grade = 80
WHERE id = 1;
-- 3. Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET math_grade = 90
WHERE id IN (2,4);
-- 4. Add 40 to the student which id is 6.
UPDATE students
SET math_grade = 40
WHERE id = 6;
-- 5. Count how many students have a grade bigger than 83
SELECT COUNT(id)
FROM students
WHERE math_grade > 83;

-- 6. Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', '1980-10-03', 70);
-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
SELECT first_name, last_name, COUNT(math_grade) as total_grade
FROM students
GROUP BY first_name, last_name;
-- Hint : Use GROUP BY.
-- SUM
-- Find the sum of all the students grades.
SELECT SUM(math_grade)
FROM students;