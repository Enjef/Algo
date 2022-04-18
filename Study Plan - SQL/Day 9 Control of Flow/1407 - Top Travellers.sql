# Write your MySQL query statement below
-- 57.60%
SELECT name, SUM(IF(distance IS NULL, 0, distance)) AS travelled_distance
FROM Users u LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY name
ORDER BY travelled_distance DESC, name
