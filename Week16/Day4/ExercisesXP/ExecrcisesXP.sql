-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.

SELECT
	m.title,
	g.genre_name,
	RANK() OVER(PARTITION BY mg.genre_id ORDER BY popularity DESC) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_genres AS mg
	ON m.movie_id = mg.movie_id
JOIN movies.genre AS g
	ON mg.genre_id = g.genre_id
ORDER BY movie_rank

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue.
--  Display the company name, movie title, revenue, and quartile.

SELECT
	pc.company_name,
	m.title,
	m.revenue,
	NTILE(4) OVER(PARTITION BY pc.company_id ORDER BY m.revenue DESC) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_company AS mc
	ON m.movie_id = mc.movie_id
JOIN movies.production_company AS pc
	ON mc.company_id = pc.company_id
ORDER BY movie_rank, pc.company_name

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre.
-- Display the genre name, movie title, budget, and running total budget.

SELECT
	g.genre_name,
	m.title,
	m.budget,
	SUM(m.budget) OVER(PARTITION BY g.genre_id ORDER BY m.runtime ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_genres AS mg
	ON m.movie_id = mg.movie_id
JOIN movies.genre AS g
	ON mg.genre_id = g.genre_id

-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date.
-- Display the genre name, movie title, and release date.

SELECT
	g.genre_name,
	m.title,
	m.release_date,
	FIRST_VALUE(m.title) OVER(PARTITION BY g.genre_id ORDER BY m.release_date DESC) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_genres AS mg
	ON m.movie_id = mg.movie_id
JOIN movies.genre AS g
	ON mg.genre_id = g.genre_id


--Exercise 2: Cast and Crew Performance Analysis

-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.

SELECT
	p.person_name,
	DENSE_RANK() OVER(ORDER BY COUNT(mc.movie_id) DESC) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_cast AS mc
	ON m.movie_id = mc.movie_id
JOIN movies.person AS p
	ON mc.person_id = p.person_id
GROUP BY p.person_name

-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. 
-- Display the director’s name and their average rating.

WITH cte AS (SELECT
	p.person_name,
	AVG(m.vote_average) AS vote_avg,
	RANK() OVER(PARTITION BY p.person_name ORDER BY AVG(m.vote_average) DESC) AS avg_rank
FROM movies.movie AS m
JOIN movies.movie_crew AS mc
	ON m.movie_id = mc.movie_id
JOIN movies.person AS p
	ON p.person_id = mc.person_id
WHERE mc.job='Director'
GROUP BY p.person_name
	)
SELECT 
	person_name,
	vote_avg
FROM cte
WHERE avg_rank = 1
ORDER BY vote_avg DESC
LIMIT 1

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
-- Display the actor’s name and the cumulative revenue.
SELECT
	p.person_name,
	SUM(m.revenue) OVER(PARTITION BY p.person_name ORDER BY m.movie_id) AS movie_rank
FROM movies.movie AS m
JOIN movies.movie_cast AS mc
	ON m.movie_id = mc.movie_id
JOIN movies.person AS p
	ON mc.person_id = p.person_id


-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. 
-- Display the director’s name and the total budget.

WITH cte_total_budget AS (SELECT
	p.person_name,
	SUM(m.budget) AS total_budget,
	DENSE_RANK() OVER(PARTITION BY p.person_name ORDER BY SUM(m.budget) DESC) AS sum_rank
FROM movies.movie AS m
JOIN movies.movie_crew AS mc
	ON m.movie_id = mc.movie_id
JOIN movies.person AS p
	ON p.person_id = mc.person_id
WHERE mc.job='Director'
GROUP BY p.person_name
	)
SELECT 
	person_name,
	total_budget
FROM cte_total_budget
WHERE sum_rank = 1
ORDER BY total_budget DESC
LIMIT 1