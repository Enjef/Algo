# Write your MySQL query statement below
-- 82.44%
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'

-- best
select *
from Patients
where conditions LIKE '% DIAB1%' or conditions LIKE 'DIAB1%'

-- 2nd best
SELECT
    Patients.patient_id, 
    Patients.patient_name, 
    Patients.conditions
from Patients
Where  
    Patients.conditions LIKE 'DIAB1%'
    or Patients.conditions LIKE '% DIAB1%'
