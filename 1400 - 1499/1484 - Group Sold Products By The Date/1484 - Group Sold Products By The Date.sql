# Write your MySQL query statement below
-- 39.26%
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date

-- best
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT(product) ORDER BY product) AS products
FROM Activities
GROUP BY sell_date

-- 2nd best
select  sell_date, count(distinct(product)) as num_sold, group_concat(distinct product order by product asc separator ',') as products
from activities
group by sell_date
order by sell_date 

-- 3d best
select sell_date, count(distinct product) as num_sold,group_concat(distinct product) as products
from activities
group by sell_date

-- 4th best
SELECT 
  sell_date, 
  COUNT(DISTINCT product) AS num_sold, 
  GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products
FROM Activities
GROUP BY sell_date 
ORDER BY sell_date ASC;
