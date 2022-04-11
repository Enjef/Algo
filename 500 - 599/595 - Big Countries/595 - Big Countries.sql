# Write your MySQL query statement below
-- 83.07%
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000

-- best
SELECT w.name, w.population, w.area
FROM World as w
WHERE w.area >= 3000000 OR w.population >= 25000000
