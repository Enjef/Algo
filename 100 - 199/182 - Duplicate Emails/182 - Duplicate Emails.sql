# Write your MySQL query statement below
SELECT email AS Email
FROM PERSON
GROUP BY email
HAVING COUNT(id) > 1

-- best
select email
from person
group by email
having count(email) > 1

-- 4
SELECT email FROM (
    SELECT email, COUNT(email) AS cnt
    FROM Person
    GROUP BY email) AS temp
    WHERE temp.cnt > 1
