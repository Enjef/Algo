# Write your MySQL query statement below
SELECT email AS Email
FROM PERSON
GROUP BY email
HAVING COUNT(id) > 1
