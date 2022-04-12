# Write your MySQL query statement below
-- 73.68%
DELETE person1 FROM Person person1, Person person2
WHERE person1.email = person2.email and person1.id > person2.id

-- best
 DELETE 
 FROM PERSON
 WHERE ID NOT IN (
     SELECT ID FROM (
         SELECT MIN(ID) AS ID
           FROM PERSON
       GROUP BY EMAIL) T)

-- 2nd best
DELETE 
FROM Person
WHERE Id NOT IN
(
    SELECT sub.min_id
    FROM 
    (SELECT Email, MIN(Id) AS min_id
    FROM Person
    GROUP BY Email) sub
)

-- 3rd best
DELETE FROM Person
WHERE Id NOT IN (
    SELECT Id
    FROM (
        SELECT MIN(Id) AS Id
        FROM Person
        GROUP BY Email
    ) AS x
)

-- 4th best
delete from Person where id not in (select min(s.id) from (select * from Person) s group by s.email);
