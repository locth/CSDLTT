local emp_list = redis.call("SMEMBERS", KEYS[1])

for _, key in ipairs(emp_list) do
    redis.call('DEL', key)
end