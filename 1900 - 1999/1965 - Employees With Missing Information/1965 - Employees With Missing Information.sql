# Write your MySQL query statement below
-- 93.90%
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;

-- best
SELECT employee_id
FROM Employees 
WHERE employee_id 
NOT IN (SELECT employee_id FROM Salaries)

UNION

SELECT employee_id
FROM Salaries 
WHERE employee_id
NOT IN (SELECT employee_id FROM Employees)

ORDER BY employee_id ASC

-- 2nd best
SELECT s.employee_id FROM Salaries s where s.employee_id not in (select e.employee_Id from Employees e)
Union
SELECT e.employee_id FROM Employees e where e.employee_id not in (select s.employee_Id from Salaries s) 
order by employee_id asc

-- 3d best
WITH ALL_EMPLOYEES
AS (SELECT employee_id FROM Employees 
    UNION 
    SELECT employee_id FROM Salaries)

SELECT employee_id FROM ALL_EMPLOYEES
WHERE
employee_id NOT IN (SELECT employee_id FROM Employees)
OR
employee_id NOT IN (SELECT employee_id FROM Salaries)
ORDER BY 1
