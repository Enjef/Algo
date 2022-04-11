# Write your MySQL query statement below
-- 48.02%
SELECT name as Customers
FROM Customers
WHERE Customers.id NOT IN (SELECT customerID FROM Orders)
