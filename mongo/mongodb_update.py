from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

print("Updating 300.024 records...")
start_time = time.time()
emp_collection.update_many({}, {'$set': {"nationality": "USA"}})
print("[MONGO BULK UPDATE] Execution time: %s" %(time.time()-start_time))

print("Updating single records...")
start_time = time.time()
emp_collection.update_one({"emp_no":500000}, {'$set': {"nationality": "Vietnam"}})
print("[MONGO SINGLE UPDATE] Execution time: %s" %(time.time()-start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

print("Updating 2.844.047 records...")
start_time = time.time()
sala_collection.update_many({}, {'$inc': {"salary": 10000}})
print("[MONGO BULK UPDATE] Execution time: %s" %(time.time()-start_time))

print("Updating single records...")
start_time = time.time()
sala_collection.update_one({"emp_no":500000}, {'$inc': {"salary": 10000}})
print("[MONGO SINGLE UPDATE] Execution time: %s" %(time.time()-start_time))

