from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

data = pd.read_csv("../employees.csv")
employees_dict = data.to_dict('records')

print("Inserting 300.024 records...")
start_time = time.time()
emp_collection.insert_many(employees_dict)
print("[MONGO INSERT] Execution time: %s" %(time.time()-start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

data = pd.read_csv("../salaries.csv")
salaries_dict = data.to_dict('records')

print("Inserting 2.844.047 records...")
start_time = time.time()
sala_collection.insert_many(salaries_dict)
print("[MONGO INSERT] Execution time: %s" %(time.time()-start_time))

