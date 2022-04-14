# Write your MySQL query statement below
-- 67.71%
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id

-- 2nd best
SELECT DISTINCT author_id AS id FROM views
WHERE author_id = viewer_id
ORDER BY author_id  ASC 

-- 3d best
SELECT DISTINCT author_id AS id
FROM Views
GROUP BY author_id, viewer_id
HAVING author_id=viewer_id
