# Write your MySQL query statement below
SELECT DISTINCT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE DATEDIFF('2019-07-27', activity_date) < 30
GROUP BY day

-- best
from activity
where activity_date > '2019-06-27' AND activity_date <= '2019-07-27'
group by activity_date

-- 2
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB("2019-07-27", INTERVAL 29 DAY) AND DATE("2019-07-27")
GROUP BY activity_date;

-- 3
SELECT
activity_date AS 'day',
COUNT(DISTINCT user_id) AS active_users
FROM
Activity
WHERE DATEDIFF('2019-07-27',activity_date)<30
GROUP BY 1

-- 4
select activity_date day, count(distinct user_id) active_users
from Activity
group by activity_date having activity_date > date_sub('2019-07-27', interval 30 day) and activity_date <='2019-07-27'
