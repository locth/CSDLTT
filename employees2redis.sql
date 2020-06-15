-- MIGRATE TABLE employees TO REDIS
-- SELECT CONCAT(
-- "*12\r\n",
-- '$', LENGTH(redis_cmd), '\r\n',redis_cmd, '\r\n','$', LENGTH(redis_key), '\r\n',redis_key, '\r\n',
-- '$', LENGTH(hkey1), '\r\n', hkey1, '\r\n','$', LENGTH(hval1), '\r\n', hval1, '\r\n',
-- '$', LENGTH(hkey2), '\r\n', hkey2, '\r\n','$', LENGTH(hval2), '\r\n', hval2, '\r\n',
-- '$', LENGTH(hkey3), '\r\n', hkey3, '\r\n','$', LENGTH(hval3), '\r\n', hval3, '\r\n',
-- '$', LENGTH(hkey4), '\r\n', hkey4, '\r\n','$', LENGTH(hval4), '\r\n', hval4, '\r\n',
-- '$', LENGTH(hkey5), '\r\n', hkey5, '\r\n','$', LENGTH(hval5), '\r\n', hval5, '\r'
-- )
-- FROM (
-- SELECT
-- 'HMSET' AS redis_cmd, CONCAT('emp_no:', emp_no) AS redis_key,
-- 'birth_date' AS hkey1, birth_date  AS hval1,
-- 'first_name' AS hkey2, first_name AS hval2,
-- 'last_name' AS hkey3, last_name AS hval3,
-- 'gender' AS hkey4, gender AS hval4,
-- 'hire_date' AS hkey5, hire_date AS hval5
--  FROM employees
--  ) AS t

-- MIGRATE TABLE salaries TO REDIS
SELECT CONCAT(
"*6\r\n",
'$', LENGTH(redis_cmd), '\r\n',redis_cmd, '\r\n','$', LENGTH(redis_key), '\r\n',redis_key, '\r\n',
'$', LENGTH(hkey1), '\r\n', hkey1, '\r\n','$', LENGTH(hval1), '\r\n', hval1, '\r\n',
'$', LENGTH(hkey2), '\r\n', hkey2, '\r\n','$', LENGTH(hval2), '\r\n', hval2, '\r\n'
)
FROM (
SELECT
'SADD' AS redis_cmd, CONCAT('emp_no:', emp_no, ' ', from_date) AS redis_key,
'salary' AS hkey1, salary  AS hval1,
'to_date' AS hkey2, to_date AS hval2
 FROM salaries
 ) AS t

-- RUN THIS COMMAND:
-- mysql -u root -p employees --skip-column-names --raw < employees2redis.sql | redis-cli --pipe