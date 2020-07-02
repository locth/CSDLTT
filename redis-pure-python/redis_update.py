import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

pipe = r.pipeline()

print("--- WORKING ON 300.024 RECORDS ---")
print("Updating 300024 records...")
start_time = time.time()
for key in r.smembers('employees'):
    pipe.hset(key, mapping = {'nationality': 'USA'})
pipe.execute()
print("[REDIS BULK UPDATE] Execution time: %s" % (time.time() - start_time))

print("Updating single records...")
start_time = time.time()
r.hset(name = 'emp_no:500000',
mapping = {
    'nationality': 'Vietnam'
})
print("[REDIS UPDATE] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")
print("Updating 2.844.047 records...")
start_time = time.time()
for key in r.smembers('salaries'):
    pipe.hincrby(key, 'salary', 10000)
pipe.execute()
print("[REDIS BULK UPDATE] Execution time: %s" % (time.time() - start_time))

print("Updating single records...")
start_time = time.time()
r.hincrby('emp_no:500000:from_date:1990-10-20', 'salary', 10000)
print("[REDIS UPDATE] Execution time: %s" % (time.time() - start_time))