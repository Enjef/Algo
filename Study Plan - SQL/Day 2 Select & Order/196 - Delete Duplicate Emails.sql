# Write your MySQL query statement below
-- 73.68%
DELETE person1 FROM Person person1, Person person2
WHERE person1.email = person2.email and person1.id > person2.id
