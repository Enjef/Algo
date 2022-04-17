# Write your MySQL query statement below
-- 18.46%
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp)=2020
GROUP BY user_id;

-- best
select user_id, max(time_stamp) as last_stamp
from Logins where time_stamp like '2020%'
group by user_id

-- 2
SELECT 
user_id,
max(time_stamp) as last_stamp
FROM 
    Logins
WHERE 
    time_stamp like "2020-%"
group by 1 
