from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

data = pd.read_csv("employees.csv")
employees_dict = data.to_dict('records')

print("Inserting 300.024 records...")
start_time = time.time()
emp_collection.insert_many(employees_dict)
print("[MONGO BULK INSERT] Execution time: %s" %(time.time()-start_time))

print("Inserting single records...")
emp_rec = {
    "emp_no": 500000,
    "birth_date": "1/1/60",
    "first_name": "John",
    "last_name": "Doe",
    "gender": "F",
    "hire_date": "10/20/90"
}
start_time = time.time()
emp_collection.insert_one(emp_rec)
print("[MONGO SINGLE INSERT] Execution time: %s" %(time.time()-start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

data = pd.read_csv("salaries.csv")
salaries_dict = data.to_dict('records')

print("Inserting 2.844.047 records...")
start_time = time.time()
sala_collection.insert_many(salaries_dict)
print("[MONGO BULK INSERT] Execution time: %s" %(time.time()-start_time))

print("Inserting single records...")
sala_rec = {
    "emp_no": 500000,
    "from_date": "10/20/90",
    "salary": 70000,
    "to_date": "10/19/91",
}
start_time = time.time()
sala_collection.insert_one(sala_rec)
print("[MONGO SINGLE INSERT] Execution time: %s" %(time.time()-start_time))

