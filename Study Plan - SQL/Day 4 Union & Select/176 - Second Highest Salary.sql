# Write your MySQL query statement below
-- 74.90%
SELECT IF(COUNT(DISTINCT id)>1, (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
FROM Employee

-- 80.22%
SELECT IF(COUNT(DISTINCT salary)>1, (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary
FROM Employee
