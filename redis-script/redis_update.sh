#!/bin/sh

echo "=== WORKING ON EMPLOYEES TABLE: 300.024 records ==="
echo "[REDIS BULK UPDATE] Execution time: "
time redis-cli --eval redis_update.lua employees

echo "[REDIS SINGLE UPDATE] Execution time: "
time redis-cli HSET emp_no:500000 nationality Vietnam

echo "=== WORKING ON EMPLOYEES TABLE: 2.844.047 records ==="
echo "[REDIS BULK UPDATE] Execution time: "
time redis-cli --eval redis_update.lua salaries

echo "[REDIS SINGLE UPDATE] Execution time: "
time redis-cli HINCRBY emp_no:500000:from_date:10-20-1990 salary 10000