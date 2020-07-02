import redis
import time

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password=''
)

script = '''
local emp_list = redis.call("SMEMBERS", KEYS[1])
local count = 0

for _, key in ipairs(emp_list) do
    redis.call('DEL', key)
    count = count + 1
end

print(count.." KEYS HAVE BEEN DELETED")
'''

print("--- WORKING ON 300.024 RECORDS ---")

start_time = time.time()
r.eval(script, 1, 'employees')
print("[REDIS DELETE BY LUA] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")

start_time = time.time()
r.eval(script, 1, 'salaries')
print("[REDIS QUERY BY LUA] Execution time: %s" % (time.time() - start_time))