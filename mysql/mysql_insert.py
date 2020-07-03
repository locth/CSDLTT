import mysql.connector
import csv
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hoangvanhieu",
  database="testdb"
)

mycursor = mydb.cursor()

print("--- WORKING ON 300.024 RECORDS ---")
with open('../employees.csv', newline='') as f:
    reader = csv.reader(f)
    emp_list = [tuple(row) for row in reader]

sql = "INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (%s, %s, %s, %s, %s, %s)"

start_time = time.time()
mycursor.executemany(sql, emp_list[1:])
mydb.commit()
print("[MYSQL INSERT] Execution time: %s" %(time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
with open('../salaries.csv', newline='') as f:
    reader = csv.reader(f)
    sala_list = [tuple(row) for row in reader]

sql = "INSERT INTO salaries (emp_no, salary, from_date, to_date) VALUES (%s, %s, %s, %s)"

start_time = time.time()
mycursor.executemany(sql, sala_list[1:700000])
mycursor.executemany(sql, sala_list[700000:1400000])
mycursor.executemany(sql, sala_list[1400000:2100000])
mycursor.executemany(sql, sala_list[2100000:])
mydb.commit()
print("[MYSQL INSERT] Execution time: %s" %(time.time() - start_time))