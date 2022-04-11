# Write your MySQL query statement below
-- 76.98%
UPDATE Salary
SET sex = IF(sex='m', 'f', 'm')

-- best
UPDATE Salary
SET sex = CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END

-- 4th best

UPDATE Salary
SET sex = CASE WHEN sex = "m" THEN "f"
          ELSE "m"
          END
