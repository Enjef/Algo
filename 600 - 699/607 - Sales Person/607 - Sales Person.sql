# Write your MySQL query statement below
-- 72.93%
SELECT Name
FROM SalesPerson
WHERE Name NOT IN (
    SELECT s.name 
    FROM SalesPerson s, Company c, Orders o 
    WHERE s.sales_id = o.sales_id AND o.com_id = c.com_id AND c.name = 'RED')

-- best
 select a.name from SalesPerson a 
 where a.sales_id not in (select b.sales_id from orders b 
                          join company c 
                          on b.com_id = c.com_id where name = 'RED')

-- 2nd best 
 select s.name from SalesPerson s 
 where s.sales_id not in(
    select o.sales_id
    from Orders o join Company c on o.com_id = c.com_id
    where c.name="RED")

-- 3d best
SELECT
    s.name
FROM SalesPerson s
WHERE
    s.sales_id NOT IN(
        SELECT o.sales_id
        FROM Orders o JOIN Company c
        ON o.com_id = c.com_id
        WHERE c.name = 'RED'
    )

-- 4th
SELECT
    s.name
FROM
    salesperson s
WHERE
    s.sales_id NOT IN (SELECT
            o.sales_id
        FROM
            orders o
                LEFT JOIN
            company c ON o.com_id = c.com_id
        WHERE
            c.name = 'RED');

-- 5th
select SalesPerson.name
from SalesPerson
where SalesPerson.sales_id NOT IN (
    select Orders.sales_id
    from Orders left join Company on Orders.com_id = Company.com_id
    where Company.name like "RED")
