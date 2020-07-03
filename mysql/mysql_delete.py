import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hoangvanhieu",
  database="testdb"
)

mycursor = mydb.cursor(buffered=True)

print("--- WORKING ON 300.024 RECORDS ---")
mycursor.execute("SELECT emp_no FROM employees")
emp_no_list = mycursor.fetchall()

sql = "DELETE FROM employees WHERE emp_no = %s"
start_time = time.time()
for x in emp_no_list:
  # val = (x[0],)
  mycursor.execute(sql, (x[0],))
mydb.commit()
print("[MYSQL UPDATE] Execution time: %s" %(time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
mycursor.execute("SELECT emp_no, from_date FROM salaries")
sala_no_list = mycursor.fetchall()

sql = "DELETE FROM salaries WHERE emp_no = %s AND from_date = %s"
start_time = time.time()
for x in sala_no_list:
  # val = (x[0], x[1])
  mycursor.execute(sql, (x[0], x[1]))
mydb.commit()
print("[MYSQL UPDATE] Execution time: %s" %(time.time() - start_time))