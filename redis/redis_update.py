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

if KEYS[1] == "employees" then
    for _, key in ipairs(emp_list) do
        redis.call('HSET', key, "nationality", "USA")
        count = count + 1
    end
elseif KEYS[1] == "salaries" then
    for _, key in ipairs(emp_list) do
        redis.call('HINCRBY', key, "salary", 10000)
        count = count + 1
    end
end

print (count.." KEYS HAVE BEEN UPDATED")
'''

print("--- WORKING ON 300.024 RECORDS ---")

start_time = time.time()
r.eval(script, 1, 'employees')
print("[REDIS UPDATE BY LUA] Execution time: %s" % (time.time() - start_time))

print("--- WORKING ON 2.844.047 RECORDS ---")

start_time = time.time()
r.eval(script, 1, 'salaries')
print("[REDIS UPDATE BY LUA] Execution time: %s" % (time.time() - start_time))