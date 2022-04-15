# Write your MySQL query statement below
-- 74.00%
SELECT w2.id AS id
FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w1.temperature < w2.temperature
