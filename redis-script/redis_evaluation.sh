#!/bin/sh

echo "=== WORKING ON EMPLOYEES TABLE: 300.024 records ==="
echo "[REDIS BULK INSERT] Execution time: "
time (cat redis_emp.txt | redis-cli --pipe)

echo "[REDIS SINGLE INSERT] Execution time: "
time (cat redis_single_emp.txt | redis-cli --pipe)

echo "[REDIS BULK UPDATE] Execution time: "
time redis-cli --eval redis_update.lua employees

echo "[REDIS SINGLE UPDATE] Execution time: "
time redis-cli HSET emp_no:500000 nationality Vietnam

echo "[REDIS BULK QUERY] Execution time: "
time redis-cli --eval redis_query.lua employees

echo "[REDIS SINGLE QUERY] Execution time: "
time redis-cli HGETALL emp_no:500000

echo "[REDIS SINGLE DELETE] Execution time: "
time redis-cli DEL emp_no:500000

echo "[REDIS BULK DELETE] Execution time: "
time redis-cli --eval redis_delete.lua employees

echo "=== WORKING ON EMPLOYEES TABLE: 2.844.047 records ==="
echo "[REDIS BULK INSERT] Execution time: "
time (cat redis_sala.txt | redis-cli --pipe)

echo "[REDIS SINGLE INSERT] Execution time: "
time (cat redis_single_sala.txt | redis-cli --pipe)

echo "[REDIS BULK UPDATE] Execution time: "
time redis-cli --eval redis_update.lua salaries

echo "[REDIS SINGLE UPDATE] Execution time: "
time redis-cli HINCRBY emp_no:500000:from_date:10-20-1990 salary 10000

echo "[REDIS BULK INSERT] Execution time: "
time redis-cli --eval redis_query.lua salaries

echo "[REDIS SINGLE QUERY] Execution time: "
time redis-cli HGETALL emp_no:500000:from_date:10-20-1990

echo "[REDIS SINGLE DELETE] Execution time: "
time redis-cli DEL emp_no:500000:from_date:10-20-1990

echo "[REDIS BULK DELETE] Execution time: "
time redis-cli --eval redis_delete.lua salaries