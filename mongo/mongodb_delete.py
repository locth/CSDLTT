from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

print("Deleting 300.024 records...")
start_time = time.time()
emp_collection.delete_many({})
print("[MONGO DELETE] Execution time: %s" %(time.time()-start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

print("Deleting 2.844.047 records...")
start_time = time.time()
sala_collection.delete_many({})
print("[MONGO DELETE] Execution time: %s" %(time.time()-start_time))

