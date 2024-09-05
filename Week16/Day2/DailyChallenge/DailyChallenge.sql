-- Exercise 1: Detailed Medal Analysis

-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics.
-- Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.

CREATE TEMPORARY TABLE competitors_summer_winter_medals AS
SELECT ce.competitor_id,
       SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
       SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.games g ON e.games_id = g.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;

SELECT * FROM competitors_summer_winter_medals;

--Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports.
-- Display the contents of this table.

CREATE TEMPORARY TABLE competitors_two_sports_medals AS
SELECT ce.competitor_id,
       COUNT(DISTINCT e.sport_id) AS sports_count,
       COUNT(ce.medal_id) AS total_medals
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT competitor_id, total_medals
FROM competitors_two_sports_medals
ORDER BY total_medals DESC
LIMIT 3;


-- Exercise 2: Region and Competitor Performance

-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event.
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.

WITH competitor_max_medals AS (
    SELECT ce.competitor_id, ce.event_id, COUNT(ce.medal_id) AS medals_won
    FROM olympics.competitor_event ce
    WHERE ce.medal_id IS NOT NULL
    GROUP BY ce.competitor_id, ce.event_id
    HAVING COUNT(ce.medal_id) = (
        SELECT MAX(COUNT(sub_ce.medal_id))
        FROM olympics.competitor_event sub_ce
        WHERE sub_ce.competitor_id = ce.competitor_id
        GROUP BY sub_ce.event_id
    )
)

SELECT pr.region_id, SUM(cm.medals_won) AS total_medals
FROM competitor_max_medals cm
JOIN olympics.person_region pr ON cm.competitor_id = pr.person_id
GROUP BY pr.region_id
ORDER BY total_medals DESC
LIMIT 5;

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals.
-- Retrieve and display the contents of this table, including their full names and the number of games they participated in.

CREATE TEMPORARY TABLE competitors_no_medals AS
SELECT p.id AS competitor_id, p.full_name, COUNT(DISTINCT g.id) AS games_participated
FROM olympics.person p
JOIN olympics.competitor_event ce ON p.id = ce.competitor_id
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.games g ON e.games_id = g.id
WHERE ce.medal_id IS NULL
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT g.id) > 3;

SELECT * FROM competitors_no_medals;
