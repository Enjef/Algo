# Write your MySQL query statement below
-- 43.20%
SELECT  event_day AS day, emp_id, SUM(out_time-in_time) AS total_time
FROM Employees
GROUP BY day, emp_id

-- 4
SELECT
    event_day as day,
    emp_id,
    sum(diffs) as total_time
FROM
(
SELECT
    emp_id,
    event_day,
    out_time-in_time as diffs
FROM Employees
    ) f
    GROUP BY 1,2
