# Write your MySQL query statement below
-- 80.23%
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(director_id) > 2


-- best
SELECT actor_id, director_id FROM ActorDirector 
GROUP BY actor_id, director_id
HAVING COUNT(timestamp)>=3

-- 2
SELECT
actor_id,
director_id
FROM ActorDirector
GROUP BY 1, 2
HAVING COUNT(timestamp) >= 3;
