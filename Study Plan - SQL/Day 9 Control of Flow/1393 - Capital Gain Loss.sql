# Write your MySQL query statement below
-- 5.49%
SELECT stock_name, SUM(IF(operation='BUY', -price, price)) as capital_gain_loss
FROM Stocks
GROUP BY stock_name
