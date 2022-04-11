# Write your MySQL query statement below
-- 69.89%
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2
