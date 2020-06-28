import redis
import pandas as pd
import time

col_name = ['emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date']

employees = pd.read_csv("employees.csv")

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

pipe = r.pipeline()

print("Import data from csv...")
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
    'hire_date': '10/20/20'
})
print("[REDIS SINGLE INSERT] Execution time: %s" % (time.time() - start_time))