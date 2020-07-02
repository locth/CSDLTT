from pymongo import MongoClient
import pprint
import time
import pandas as pd

client = MongoClient()
db = client['employees']

print("--- WORKING ON 300.024 RECORDS ---")
emp_collection = db['employees']

emp_list = emp_collection.find({}, {"_id":1})

print("Querying 300.024 records...")
start_time = time.time()
for doc in emp_list:
    emp_collection.find({"_id":doc["_id"]})
print("[MONGO QUERY] Execution time: %s" %(time.time()-start_time))

print([doc["emp_no"] for doc in emp_list])

print("--- WORKING ON 2.844.047 RECORDS ---")
sala_collection = db['salaries']

sala_list = sala_collection.find({}, {"_id":1})

print("Querying 2.844.047 records...")
start_time = time.time()
for doc in sala_list:
    sala_collection.find({"_id":doc["_id"]})
print("[MONGO QUERY] Execution time: %s" %(time.time()-start_time))
