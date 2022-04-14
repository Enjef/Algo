# Write your MySQL query statement below
-- 67.71%
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
