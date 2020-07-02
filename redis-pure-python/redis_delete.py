import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

pipe = r.pipeline()

print("--- WORKING ON 300.024 RECORDS ---")
print("Deleting single records...")
start_time = time.time()
r.delete('emp_no:500000')
r.srem('employees','emp_no:500000')
print("[REDIS DELETE] Execution time: %s" % (time.time() - start_time))

print("Deleting 300024 records...")
start_time = time.time()
for key in r.smembers('employees'):
    pipe.delete(key)
pipe.delete('employees')
pipe.execute()
print("[REDIS BULK DELETE] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
print("Deleting single records...")
start_time = time.time()
r.delete('emp_no:500000:from_date:1990-10-20')
r.srem('salaries','emp_no:500000:from_date:1990-10-20')
print("[REDIS DELETE] Execution time: %s" % (time.time() - start_time))

print("Deleting 2.844.047 records...")
start_time = time.time()
for key in r.smembers('salaries'):
    pipe.delete(key)
pipe.delete('salaries')
pipe.execute()
print("[REDIS BULK DELETE] Execution time: %s" % (time.time() - start_time))