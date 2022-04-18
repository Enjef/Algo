# Write your MySQL query statement below
-- 5.49%
SELECT stock_name, SUM(IF(operation='BUY', -price, price)) as capital_gain_loss
FROM Stocks
GROUP BY stock_name

-- best
select stock_name,
sum(if(operation="Sell",price,0))-
sum(if(operation="Buy",price,0))
as capital_gain_loss
from stocks
group by stock_name

-- best 2
select stock_name,
sum(case when operation = 'Buy' then -price else price end) as capital_gain_loss
from stocks
group by 1;

-- 3
select stock_name, Sum(case when operation= 'Buy' then -price else price end) as capital_gain_loss
from stocks
group by stock_name

-- 4
SELECT DISTINCT s1.stock_name, (s2.price-s1.price) AS capital_gain_loss
FROM
(
    SELECT stock_name, SUM(price) AS price
    FROM Stocks
    WHERE operation="Buy"
    GROUP BY stock_name
) AS s1 JOIN
(
    SELECT stock_name, SUM(price) AS price
    FROM Stocks
    WHERE operation="Sell"
    GROUP BY stock_name
) AS s2
ON s1.stock_name=s2.stock_name
