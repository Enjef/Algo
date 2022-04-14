# Write your MySQL query statement below
-- 82.89%
SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address
ON Person.personId = Address.personId

-- best
select p.firstName,
p.lastName,
a.city,
coalesce(a.state,null) as state
from person p
left join address a
on p.personId=a.personId

-- 2nd best
select p.firstName,p.lastname, a.city, a.state
from Person p
left join Address a on p.personId=a.PersonId
