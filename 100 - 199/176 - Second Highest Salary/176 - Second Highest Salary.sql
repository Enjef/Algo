# Write your MySQL query statement below
-- 74.90%
SELECT IF(COUNT(DISTINCT id)>1, (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
FROM Employee

-- 80.22%
SELECT IF(COUNT(DISTINCT salary)>1, (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
FROM Employee

-- best
SELECT
    IFNULL((SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1), NULL) as SecondHighestSalary

-- 2nd best
SELECT MAX(salary) as SecondHighestSalary
FROM Employee 
WHERE salary < ( SELECT MAX(salary) FROM Employee )

-- 3d best
select max(salary) as  SecondHighestSalary 
from(select salary,dense_rank() over(order by salary desc) rr from employee)ee
where rr=2;

-- 4th best
Select 
(Select DISTINCT salary 
from Employee
Order BY salary Desc
Limit 1 Offset 1) AS SecondHighestSalary;
