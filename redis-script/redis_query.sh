#!/bin/sh

echo "=== WORKING ON EMPLOYEES TABLE: 300.024 records ==="
echo "[REDIS BULK QUERY] Execution time: "
time redis-cli --eval redis_query.lua employees

echo "[REDIS SINGLE QUERY] Execution time: "
time redis-cli HGETALL emp_no:500000

echo "=== WORKING ON EMPLOYEES TABLE: 2.844.047 records ==="
echo "[REDIS BULK INSERT] Execution time: "
time redis-cli --eval redis_query.lua salaries

echo "[REDIS SINGLE QUERY] Execution time: "
time redis-cli HGETALL emp_no:500000:from_date:10-20-1990