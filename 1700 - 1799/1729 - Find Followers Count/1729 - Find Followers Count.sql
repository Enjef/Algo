# Write your MySQL query statement below
-- 95.67%
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id

-- best
select user_id , count(*) as followers_count from Followers
group by user_id
order by user_id
