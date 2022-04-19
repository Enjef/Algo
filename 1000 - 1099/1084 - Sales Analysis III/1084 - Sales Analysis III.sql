# Write your MySQL query statement below
SELECT p.product_id, product_name
FROM Product p LEFT JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING DATE(MIN(s.sale_date)) >= '2019-01-01' AND DATE(MAX(s.sale_date)) <= '2019-03-31'

-- best
with CTE as (
    select product_id
    from Sales
    where sale_date not between "2019-01-01" and "2019-03-31"
)
select p.product_id, p.product_name
from product p
where not exists (select * from CTE c where p.product_id = c.product_id)

-- 2
SELECT
    product_id,
    product_name
FROM Product
WHERE product_id NOT IN (
    SELECT Product.product_id
    FROM Sales
    JOIN Product
    USING (product_id)
    WHERE sale_date NOT BETWEEN "2019-01-01" AND "2019-03-31"
);

-- 3
SELECT s.product_id, product_name
FROM Sales s
LEFT JOIN Product p
ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(sale_date) >= CAST('2019-01-01' AS DATE) AND
       MAX(sale_date) <= CAST('2019-03-31' AS DATE)

-- 4
with data as 
(select product_id, 
    sum(if(sale_date between '2019-01-01' and '2019-03-31',0,1)) as summa
    from
(select p.*, s.sale_date
    from Product p join Sales s 
    on p.product_id=s.product_id) as t
    group by product_id)

select p.product_id, product_name
    from Product p join data
    on p.product_id=data.product_id
    where data.summa=0

-- 5
select a.product_id, a.product_name
from Product a, (select product_id, min(sale_date) as min_date,
                 max(sale_date) as max_date from Sales group by product_id) b
where a.product_id=b.product_id 
    and b.min_date >= '2019-01-01' and b.max_date <= '2019-03-31'
    ;

-- 6
select product_id, product_name from product where product_id not in ( 
select product_id from sales
where sale_date not between '2019-01-01' and '2019-03-31')
