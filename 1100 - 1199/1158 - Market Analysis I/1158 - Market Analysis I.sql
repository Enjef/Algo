# Write your MySQL query statement below
-- 32.32%
SELECT u.user_id AS buyer_id, join_date, IFNULL(COUNT(order_date), 0) AS orders_in_2019
FROM Users u LEFT JOIN Orders o ON (u.user_id = o.buyer_id AND YEAR(order_date) = '2019')
GROUP BY u.user_id

-- best
select
    u.user_id as buyer_id,
    u.join_date,
    coalesce(count(o.order_id),0) as orders_in_2019
from users u
left join orders o on o.buyer_id=u.user_id and year(order_date)='2019'
group by 1,2

-- 2
select a.user_id as buyer_id,b.join_date ,a.cnt as orders_in_2019 from(
select user_id,count(order_id)cnt from users left join
orders on users.user_id=orders.buyer_id
and year(ordeR_date)=2019
group by user_id) a join users b on a.user_id=b.user_id

-- 3
SELECT
    u.user_id AS buyer_id,
    u.join_date AS join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
        AND o.order_date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY u.user_id, u.join_date

-- 4
select t1.user_id as buyer_id, t1.join_date as join_date, coalesce(t2.cnt,0) as orders_in_2019 
from 
(select distinct user_id,join_date from Users)t1
left outer join
(
select buyer_id,
year(order_date) as order_year,count(*) as cnt 
from 
Orders
where year(order_date)='2019'
group by buyer_id,year(order_date) 
order by buyer_id
)t2
on t1.user_id = t2.buyer_id
