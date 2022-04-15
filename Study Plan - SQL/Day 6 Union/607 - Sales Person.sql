# Write your MySQL query statement below
-- 72.93%
SELECT Name
FROM SalesPerson
WHERE Name NOT IN (
    SELECT s.name 
    FROM SalesPerson s, Company c, Orders o 
    WHERE s.sales_id = o.sales_id AND o.com_id = c.com_id AND c.name = 'RED')
