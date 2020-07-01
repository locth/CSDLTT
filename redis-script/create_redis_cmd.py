import redis
import pandas as pd
import time

print("--- WORKING ON 300.024 RECORDS ---")
employees = pd.read_csv("CSDLTT/employees.csv")

print("Creating file *.txt from employees.csv...")

emp_file = open("redis_emp.txt", "w+")

for i in range(0,300024):
    emp_no = employees['emp_no'][i]
    birth_date = employees['birth_date'][i]
    first_name = employees['first_name'][i]
    last_name = employees['last_name'][i]
    gender = employees['gender'][i]
    hire_date = employees['hire_date'][i]

    emp_file.write("HSET emp_no:" + str(emp_no) +
    " birth_date " + birth_date +
    " first_name " + first_name +
    " last_name " + last_name +
    " gender " + gender +
    " hire_date " + hire_date + "\n")

    emp_file.write("SADD employees emp_no:" + str(emp_no) + "\n")

emp_file.close()

print("--- WORKING ON 2.844.047 RECORDS ---")
salaries = pd.read_csv("CSDLTT/salaries.csv")
sala_file = open("redis_sala.txt", "w+")

print("Creating file *.txt from salaries.csv...")
for i in range(0,2844047):
    emp_no = salaries['emp_no'][i]
    from_date = salaries['from_date'][i]
    salary = salaries['salary'][i]
    to_date = salaries['to_date'][i]

    sala_file.write("HSET emp_no:" + str(emp_no) + ":from_date:" + from_date +
    " salary " + str(salary) +
    " to_date " + to_date + "\n")

    sala_file.write("SADD salaries emp_no:" + str(emp_no) + ":from_date:" + from_date)

sala_file.close()
