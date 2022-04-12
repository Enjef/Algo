# Write your MySQL query statement below
-- 69.79%
SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) as name
FROM Users
ORDER BY user_id

-- best
SELECT
    user_id,
    CONCAT(
        UPPER(LEFT(name,1)),
        LOWER(SUBSTRING(name,2))
        ) AS name
FROM Users
ORDER BY user_id

-- 2nd best
select user_id, CASE CHAR_LENGTH(name) WHEN 0 THEN '' ELSE CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) END as 'name'
    from Users
    order by 1

-- 3d best
select user_id, concat(upper(substring(name,1,1)),lower(substring(name,2))) as name
from Users
order by user_id;
