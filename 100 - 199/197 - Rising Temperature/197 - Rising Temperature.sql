# Write your MySQL query statement below
-- 74.00%
SELECT w2.id AS id
FROM Weather w1 JOIN Weather w2 ON DATEDIFF(w2.recordDate, w1.recordDate) = 1
WHERE w1.temperature < w2.temperature

-- best
select a.id as id
from weather a
join weather b on TO_DAYS(a.recordDate)=TO_DAYS(b.recordDate)+1
where a.temperature > b.temperature

-- 2nd best
SELECT b.id FROM Weather AS a, Weather AS b
WHERE DATE_ADD(a.recordDate, INTERVAL 1 DAY)=b.recordDate AND b.temperature>a.temperature

-- 3d best
select t.id from weather as t
INNER JOIN
Weather as y
ON t.recordDate=y.recordDate+ INTERVAL 1 DAY
AND
t.temperature > y.temperature

-- 4th best
WITH cte AS (
SELECT id, recordDate, temperature, LAG(recordDate) OVER(ORDER BY recordDate) AS d, LAG(temperature) OVER(ORDER BY recordDate) AS lg FROM Weather)
SELECT id FROM cte WHERE lg<temperature AND DATEDIFF(recordDate, d)=1
