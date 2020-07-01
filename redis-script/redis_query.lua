-- local collate = function (key)
--     local raw_data = redis.call('HGETALL', key)
--     local data = {}
--     for idx = 1, #raw_data, 2 do
--       data[raw_data[idx]] = raw_data[idx + 1]
--     end
  
--     return data;
-- end

-- local data = {}
-- local count = 0

local emp_list = redis.call("SMEMBERS", KEYS[1])

for _, key in ipairs(emp_list) do
    redis.call('HGETALL', key)
end