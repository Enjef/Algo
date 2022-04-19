# Write your MySQL query statement below
SELECT u.name, SUM(amount) AS balance
FROM Users u LEFT JOIN Transactions t ON u.account = t.account
GROUP BY u.name
HAVING balance > 10000

-- 3
SELECT
    U.name,
    SUM(T.amount) AS balance
FROM Users U
INNER JOIN Transactions T ON T.account = U.account
GROUP BY U.account
HAVING SUM(T.amount) > 10000

-- 4
select name, balance
from (select U.name, sum(T.amount) as balance
from Users U
inner join Transactions T on U.account = T.account
group by T.account) as A
where balance >10000

-- 5
select name, balance 
from (select account, sum(amount) as balance from transactions
        group by account
        having sum(amount) > 10000) t1
left join users u
on t1.account = u.account
