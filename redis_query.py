import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

pipe = r.pipeline()

start_time = time.time()
for emp in r.smembers('employees'):
    pipe.hgetall(emp)
pipe.execute()
print("[REDIS QUERY] Execution time: %s" % (time.time() - start_time))