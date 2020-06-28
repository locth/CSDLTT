import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

print("Inserting data to redis database...")

start_time = time.time()
r.hset(name = 'emp_no:500000',
mapping = {
    'birth_date': '1/1/60',
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'F',
    'hire_date': '10/20/20'
})
print("Redis INSERT execution time: %s" % (time.time() - start_time))