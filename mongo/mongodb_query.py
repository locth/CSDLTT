from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

print("Querying 300.024 records...")
start_time = time.time()
emp_collection.find()
print("[MONGO QUERY] Execution time: %s" %(time.time()-start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

print("Querying 2.844.047 records...")
start_time = time.time()
sala_collection.find()
print("[MONGO QUERY] Execution time: %s" %(time.time()-start_time))

