# Write your MySQL query statement below
-- 82.89%
SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address
ON Person.personId = Address.personId
