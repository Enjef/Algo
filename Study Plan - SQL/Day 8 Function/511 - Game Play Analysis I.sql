# Write your MySQL query statement below
-- 28.55%
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
