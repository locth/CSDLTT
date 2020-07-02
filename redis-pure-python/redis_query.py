import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

pipe = r.pipeline()

print("--- WORKING ON 300.024 RECORDS ---")
print("Querying 300024 records...")
start_time = time.time()
for key in r.smembers('employees'):
    pipe.hgetall(key)
pipe.execute()
print("[REDIS BULK QUERY] Execution time: %s" % (time.time() - start_time))

print("Querying single records...")
start_time = time.time()
r.hgetall('emp_no:500000')
print("[REDIS QUERY] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
print("Querying 2.844.047 records...")
start_time = time.time()
for key in r.smembers('salaries'):
    pipe.hgetall(key)
pipe.execute()
print("[REDIS BULK QUERY] Execution time: %s" % (time.time() - start_time))

print("Querying single records...")
start_time = time.time()
r.hgetall('emp_no:500000:from_date:1990-10-20')
print("[REDIS QUERY] Execution time: %s" % (time.time() - start_time))