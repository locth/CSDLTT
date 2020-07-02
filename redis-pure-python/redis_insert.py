import redis
import pandas as pd
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='',
)

pipe = r.pipeline(transaction=False)

print("--- WORKING ON 300.024 RECORDS ---")
employees = pd.read_csv("../employees.csv")

print("Import data from employees.csv...")
for i in range(0,300024):
    pipe.sadd('employees', 'emp_no:' + str(employees['emp_no'][i]))

print("Inserting 300024 records...")
start_time = time.time()
pipe.execute()
print("[REDIS BULK INSERT] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
salaries = pd.read_csv("../salaries.csv")

print("Import data from salaries.csv...")
for i in range(0,2844047):
    pipe.sadd('salaries', 'emp_no:' + str(salaries['emp_no'][i]) + ':from_date:' + str(salaries['from_date'][i]))

print("Inserting 2.844.047 records...")
start_time = time.time()
pipe.execute()
print("[REDIS BULK INSERT] Execution time: %s" % (time.time() - start_time))