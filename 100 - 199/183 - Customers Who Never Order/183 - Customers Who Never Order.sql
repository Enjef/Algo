# Write your MySQL query statement below
-- 48.02%
SELECT name as Customers
FROM Customers
WHERE Customers.id NOT IN (SELECT customerID FROM Orders)

-- best
select c.name as Customers
from Customers c
left join Orders o
on c.id = o.CustomerId
where  o.CustomerId IS NULL

-- 2nd best
select name as Customers from Customers
where id not in (select customerId from orders)

-- 4th best
select name as Customers from Customers where id not in(
select distinct customerId from Orders)
