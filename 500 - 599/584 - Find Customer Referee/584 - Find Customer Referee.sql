# Write your MySQL query statement below
-- 69.89%
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2

-- best
SELECT name from Customer
WHERE referee_id IS NULL OR referee_id <> 2

-- 2nd best
SELECT name        
FROM Customer
WHERE id NOT IN (SELECT id FROM Customer WHERE referee_id = 2 )
