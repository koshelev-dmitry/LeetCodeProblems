SELECT * FROM employee
ORDER BY salary;

SELECT sex, SUM(salary)/COUNT(sex) 
FROM employee
GROUP BY sex;

SELECT *
FROM client
WHERE client_name LIKE '%LLC';

SELECT first_name as foo
FROM employee
UNION 
SELECT second_name as bar
FROM employee;


