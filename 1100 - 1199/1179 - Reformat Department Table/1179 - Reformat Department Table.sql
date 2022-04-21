# Write your MySQL query statement below
SELECT id,
    SUM(IF(month="Jan", revenue, NULL)) AS Jan_Revenue,
    SUM(IF(month="Feb", revenue, NULL)) AS Feb_Revenue,
    SUM(IF(month="Mar", revenue, NULL)) AS Mar_Revenue,
    SUM(IF(month="Apr", revenue, NULL)) AS Apr_Revenue,
    SUM(IF(month="May", revenue, NULL)) AS May_Revenue,
    SUM(IF(month="Jun", revenue, NULL)) AS Jun_Revenue,
    SUM(IF(month="Jul", revenue, NULL)) AS Jul_Revenue,
    SUM(IF(month="Aug", revenue, NULL)) AS Aug_Revenue,
    SUM(IF(month="Sep", revenue, NULL)) AS Sep_Revenue,
    SUM(IF(month="Oct", revenue, NULL)) AS Oct_Revenue,
    SUM(IF(month="Nov", revenue, NULL)) AS Nov_Revenue,
    SUM(IF(month="Dec", revenue, NULL)) AS Dec_Revenue
FROM Department
GROUP BY id;

-- 1
select id, 
max(case when month ="Jan" then revenue end) as Jan_Revenue,
max(case when month ="Feb" then revenue end) as Feb_Revenue,
max(case when month ="Mar" then revenue end) as Mar_Revenue,
max(case when month ="Apr" then revenue end) as Apr_Revenue,
max(case when month ="May" then revenue end) as May_Revenue,
max(case when month ="Jun" then revenue end) as Jun_Revenue,
max(case when month ="Jul" then revenue end) as Jul_Revenue,
max(case when month ="Aug" then revenue end) as Aug_Revenue,
max(case when month ="Sep" then revenue end) as Sep_Revenue,
max(case when month ="Oct" then revenue end) as Oct_Revenue,
max(case when month ="Nov" then revenue end) as Nov_Revenue,
max(case when month ="Dec" then revenue end) as Dec_Revenue
from Department
group by id
;

-- 2
SELECT id,
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE NULL END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE NULL END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE NULL END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'Apr' THEN revenue ELSE NULL END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'May' THEN revenue ELSE NULL END) AS May_Revenue,
    SUM(CASE WHEN month = 'Jun' THEN revenue ELSE NULL END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'Jul' THEN revenue ELSE NULL END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'Aug' THEN revenue ELSE NULL END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'Sep' THEN revenue ELSE NULL END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'Oct' THEN revenue ELSE NULL END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'Nov' THEN revenue ELSE NULL END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'Dec' THEN revenue ELSE NULL END) AS Dec_Revenue
FROM department
GROUP BY id
