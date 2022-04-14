# Write your MySQL query statement below
-- 5.06%
SELECT customer_id, COUNT(customer_id) AS count_no_trans 
FROM Visits LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id

-- best
select customer_id, count(visit_id) as count_no_trans FROM
    (select customer_id, visit_id from Visits V where v.visit_id not in (select visit_id from Transactions))T
    Group by(Customer_id)

-- 2nd best
SELECT a.customer_id, COUNT(a.visit_id) AS count_no_trans 
FROM Visits a
LEFT JOIN Transactions b
ON a.visit_id=b.visit_id
WHERE b.transaction_id is NULL
GROUP BY a.customer_id

-- 3d best
select distinct customer_id, count(customer_id) as count_no_trans
from Visits
where visit_id
NOT IN
(
select distinct visit_id 
from Transactions
)
group by customer_id

-- 4d best
SELECT 
  customer_id,
  COUNT(1) count_no_trans
FROM visits v
  LEFT OUTER JOIN transactions t
    ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id
