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
employees = pd.read_csv("employees.csv")

print("Import data from employees.csv...")
for i in range(0,300024):
    pipe.hset(name = 'emp_no:' + str(employees['emp_no'][i]),
    mapping = {
        'birth_date': employees['birth_date'][i],
        'first_name': employees['first_name'][i],
        'last_name': employees['last_name'][i],
        'gender': employees['gender'][i],
        'hire_date': employees['hire_date'][i]
    })
    pipe.sadd('employees', 'emp_no:' + str(employees['emp_no'][i]))

print("Inserting 300024 records...")
start_time = time.time()
pipe.execute()
print("[REDIS BULK INSERT] Execution time: %s" % (time.time() - start_time))

print("Inserting single records...")
start_time = time.time()
r.hset(name = 'emp_no:500000',
mapping = {
    'birth_date': '1/1/60',
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'F',
    'hire_date': '10/20/90'
})
r.sadd('employees', 'emp_no:500000')
print("[REDIS SINGLE INSERT] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
salaries = pd.read_csv("salaries.csv")

print("Import data from salaries.csv...")
for i in range(0,2844047):
    pipe.hset(name = 'emp_no:' + str(salaries['emp_no'][i]) + ':from_date:' + str(salaries['from_date'][i]),
    mapping = {
        'salary': int(salaries['salary'][i]),
        'to_date': salaries['to_date'][i]
    })
    pipe.sadd('salaries', 'emp_no:' + str(salaries['emp_no'][i]) + ':from_date:' + str(salaries['from_date'][i]))

print("Inserting 2.844.047 records...")
start_time = time.time()
pipe.execute()
print("[REDIS BULK INSERT] Execution time: %s" % (time.time() - start_time))

print("Inserting single records...")
start_time = time.time()
r.hset(name = 'emp_no:500000:from_date:1990-10-20',
mapping = {
    'salary': 70000,
    'to_date': '1991-10-19',
})
r.sadd('salaries', 'emp_no:500000:from_date:1990-10-20')
print("[REDIS SINGLE INSERT] Execution time: %s" % (time.time() - start_time))