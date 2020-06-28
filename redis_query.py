import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

print("Querying 300024 records...")
start_time = time.time()
r.smembers('employees')
print("[REDIS QUERY] Execution time: %s" % (time.time() - start_time))

print("Querying single records...")
start_time = time.time()
r.hgetall('emp_no:500000')
print("[REDIS QUERY] Execution time: %s" % (time.time() - start_time))

# To query detail of each record, run the code below:
# pipe = r.pipeline()

# for emp in r.smembers('employees'):
#     pipe.hgetall(emp)
# pipe.execute()