#!/bin/sh

echo "=== WORKING ON EMPLOYEES TABLE: 300.024 records ==="
echo "[REDIS SINGLE DELETE] Execution time: "
time redis-cli DEL emp_no:500000

echo "[REDIS BULK DELETE] Execution time: "
time redis-cli --eval redis_delete.lua employees

echo "=== WORKING ON EMPLOYEES TABLE: 2.844.047 records ==="
echo "[REDIS SINGLE DELETE] Execution time: "
time redis-cli DEL emp_no:500000:from_date:10-20-1990

echo "[REDIS BULK DELETE] Execution time: "
time redis-cli --eval redis_delete.lua salaries