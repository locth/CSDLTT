local emp_list = redis.call("SMEMBERS", KEYS[1])
local count = 0

for _, key in ipairs(emp_list) do
    redis.call('HGETALL', key)
    count = count + 1
end

print(count.."KEYS HAVE BEEN QUERIED")