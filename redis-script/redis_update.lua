local emp_list = redis.call("SMEMBERS", KEYS[1])

if KEYS[1] == "employees" then
    for _, key in ipairs(emp_list) do
        redis.call('HSET', key, "nationality", "USA")
    end
elseif KEYS[1] == "salaries" then
    for _, key in ipairs(emp_list) do
        redis.call('HINCRBY', key, "salary", 10000)
    end
end