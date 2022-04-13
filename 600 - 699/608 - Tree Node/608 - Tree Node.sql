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

-- best
select distinct t1.id, 
case when t1.p_id is null then 'Root'
            when t2.p_id is null then 'Leaf'
            else 'Inner' end as type
from Tree t1
left join Tree t2 on t1.id = t2.p_id

-- 2nd best
select
    a.id
    ,case when a.p_id is null then 'Root'
        when b.num is not null then 'Inner'
        else 'Leaf' end as type
from(
    select *
    from Tree  
)a
left join(
    select distinct p_id as num
    from Tree
    where p_id is not null
)b
on a.id = b.num

-- 3d best
select id,
case when p_id is null then 'Root'
when id in (select p_id from tree) and p_id is not null then 'Inner'
ELSE 'Leaf' END AS type
from tree

--4th best
SELECT id,
CASE WHEN p_id is null THEN 'Root'
WHEN id not in (SELECT p_id FROM Tree WHERE p_id is not null) THEN 'Leaf'
ELSE 'Inner' END AS type
FROM Tree
