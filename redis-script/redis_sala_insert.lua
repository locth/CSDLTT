local function Split(s, delimiter)
    local result = {};
    for match in (s..delimiter):gmatch("(.-)"..delimiter) do
        table.insert(result, match);
    end
    return result;
end

for i = 1, #KEYS do
    local argv = Split(KEYS[i], ',')
    redis.call('hmset', argv[1], argv[2], argv[3], argv[4], argv[5])
    redis.call('sadd', 'salaries', argv[1])
end