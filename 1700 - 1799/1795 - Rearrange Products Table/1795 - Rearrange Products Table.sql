# Write your MySQL query statement below
-- 31.03%
SELECT product_id, 'store1' AS store, store1 as price
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 as price
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 as price
FROM Products
WHERE store3 IS NOT NULL

-- best
select product_id, "store1" as store, store1 as price
from products
where store1 is not null

union

select product_id, "store2" as store, store2 as price
from products
where store2 is not null

union 

select product_id, "store3" as store, store3 as price
from products
where store3 is not null

-- 3d best
SELECT * FROM
(SELECT product_id, 'store1' AS store, store1 as price FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 as price FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 as price FROM Products
WHERE store3 IS NOT NULL) AS T
