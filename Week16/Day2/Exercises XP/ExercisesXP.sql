-- Task 1: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events.
-- Use nested subqueries to filter and aggregate the data.
SELECT medal.medal_name, AVG(competitor.age)
	FROM olympics.competitor_event AS event
	JOIN olympics.games_competitor AS competitor
		ON event.competitor_id = competitor.id
	JOIN olympics.medal AS medal
		ON event.medal_id = medal.id
GROUP BY medal.medal_name;


-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated
-- in more than 3 different events. Use nested subqueries to filter and aggregate the data.
SELECT region.region_id,
	COUNT(DISTINCT region.person_id) AS number_of_persons
FROM olympics.person_region AS region
JOIN olympics.games_competitor AS competitor
	ON region.person_id=competitor.person_id
WHERE competitor.id IN (SELECT event.competitor_id
						FROM olympics.competitor_event AS event
						GROUP BY event.competitor_id
						HAVING COUNT(DISTINCT event.event_id)>3 )
GROUP BY region.region_id
ORDER BY number_of_persons DESC
LIMIT 5

-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter
-- to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
CREATE TEMPORARY TABLE competitor_medals AS
SELECT competitor_id, COUNT(medal_id) AS total_medals
FROM olympics.competitor_event
WHERE medal_id IS NOT NULL
GROUP BY competitor_id;

SELECT competitor_id, total_medals
FROM competitor_medals
WHERE total_medals > 2;

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors
-- who have not won any medals from a temporary table created for analysis.

DELETE FROM competitor_analysis
WHERE competitor_id IN (
    SELECT competitor_id
    FROM competitor_analysis
    WHERE total_medals = 0
);


-- Exercise 2: Advanced Data Manipulation and Optimization

-- Task 1: Update the heights of competitors based on the average height of competitors from the same region.
-- Use a correlated subquery within the UPDATE statement.

UPDATE olympics.person AS person
SET height = (
	SELECT AVG(person2.height)
	FROM olympics.person AS person2
	JOIN olympics.person_region AS region
	ON person2.id = region.person_id
	WHERE region_id = (
				        SELECT region2.region_id
				        FROM olympics.person_region AS region2
				        WHERE region2.person_id = person.id
						LIMIT 1
    					)
		     )
WHERE person.height IS NOT NULL;

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games
-- and list their total number of events participated. Use nested subqueries for filtering.
CREATE TEMPORARY TABLE multi_event_competitors AS
SELECT competitor_id, COUNT(event_id) AS total_events
FROM olympics.competitor_event
WHERE event_id IN (
    SELECT event_id
    FROM olympics.competitor_event ce_inner
    WHERE ce_inner.competitor_id = olympics.competitor_event.competitor_id
    GROUP BY ce_inner.event_id, ce_inner.competitor_id
    HAVING COUNT(ce_inner.event_id) > 1
)
GROUP BY competitor_id
HAVING COUNT(event_id) > 1;

-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. 
-- Use subqueries to calculate and compare averages.
SELECT region_id
FROM (
    SELECT pr.region_id, AVG(medal_count) AS avg_medals_per_competitor
    FROM (
        SELECT ce.competitor_id, COUNT(ce.medal_id) AS medal_count
        FROM olympics.competitor_event ce
        GROUP BY ce.competitor_id
    ) AS competitor_medals
    JOIN olympics.person_region pr ON competitor_medals.competitor_id = pr.person_id
    GROUP BY pr.region_id
) AS region_avg
WHERE region_avg.avg_medals_per_competitor > (
    SELECT AVG(medal_count)
    FROM (
        SELECT ce.competitor_id, COUNT(ce.medal_id) AS medal_count
        FROM olympics.competitor_event ce
        GROUP BY ce.competitor_id
    ) AS overall_medals
);

-- Task 4: Create a temporary table to track competitors’ participation across different seasons
-- and identify those who have participated in both Summer and Winter games.

CREATE TEMPORARY TABLE competitor_seasons AS
SELECT ce.competitor_id,
       STRING_AGG(DISTINCT g.season, ', ') AS seasons_participated
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.games g ON e.games_id = g.id
GROUP BY ce.competitor_id;

SELECT competitor_id
FROM competitor_seasons
WHERE seasons_participated LIKE '%Summer%' 
  AND seasons_participated LIKE '%Winter%';
