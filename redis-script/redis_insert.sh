#!/bin/sh

echo "=== WORKING ON EMPLOYEES TABLE: 300.024 records ==="
echo "[REDIS BULK INSERT] Execution time: "
time (cat redis_emp.txt | redis-cli --pipe)

echo "[REDIS SINGLE INSERT] Execution time: "
time (cat redis_single_emp.txt | redis-cli --pipe)

echo "=== WORKING ON EMPLOYEES TABLE: 2.844.047 records ==="
echo "[REDIS BULK INSERT] Execution time: "
time (cat redis_sala.txt | redis-cli --pipe)

echo "[REDIS SINGLE INSERT] Execution time: "
time (cat redis_single_sala.txt | redis-cli --pipe)