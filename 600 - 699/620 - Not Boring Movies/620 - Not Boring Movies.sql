# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM Cinema
WHERE (id % 2 != 0) and description NOT LIKE "boring"
ORDER BY rating DESC;

-- 1
select * from Cinema 
where mod(id,2)=1 AND description <> 'boring'
order by rating DESC;

-- 5
Select id, movie, description, rating from cinema where id%2 = 1 and description != 'boring' order by rating desc

-- 7
SELECT id, movie, description, rating
FROM Cinema
WHERE id NOT IN (
    SELECT id 
    FROM Cinema
    WHERE description = 'boring'
)
AND id % 2 = 1
ORDER BY rating DESC
