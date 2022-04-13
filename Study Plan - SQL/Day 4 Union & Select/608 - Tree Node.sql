# Write your MySQL query statement below
-- 83.90%
SELECT 
    id,
    CASE 
        WHEN p_id is NULL 
           THEN "Root"
        WHEN id IN (SELECT p_id FROM Tree)
           THEN "Inner"
        ELSE "Leaf"
    END AS type
FROM Tree
