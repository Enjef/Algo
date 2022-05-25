# Write your MySQL query statement below
-- 19.66% 100.00%
SELECT e.name as Employee
FROM Employee e JOIN Employee m ON m.id = e.managerId
WHERE m.salary < e.salary;

-- 1
Select e1.name Employee
From Employee e1 
Left Join Employee e2 On e1.managerID = e2.id
Where e1.salary > e2.salary;

-- 2
Select A.name as Employee
from Employee A, Employee B 
where A.salary > B.salary
and A.managerid = B.id

-- 3
SELECT Employee.name as Employee
FROM Employee
     INNER JOIN employee as Manager ON Employee.managerId = Manager.id
WHERE Employee.salary > Manager.salary

-- 4
select e.name as Employee 
from
Employee e join Employee m
on (e.managerId = m.id and m.salary < e.salary)
