import redis
import pandas as pd
import time
import multiprocessing as mul

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='',
    decode_responses=True
)

pipe = r.pipeline(transaction=False)

print("--- WORKING ON 300.024 RECORDS ---")

lua_file = open("../redis-script/redis_emp_insert.lua", "r")
script = lua_file.read()

emp_list = []

employees = pd.read_csv("../employees.csv")

def importEmp(i):
    emp_list.append("emp_no:" + str(employees['emp_no'][i]) +
    ",birth_day," + employees['birth_date'][i] +
    ",first_name," + employees['first_name'][i] + 
    ",last_name," + employees['last_name'][i] +
    ",gender," + employees['gender'][i] +
    ",hire_date," + employees['hire_date'][i])

print("Import data from employees.csv...")
start_time = time.time()
for i in range (0, 300024):
    importEmp(i)

print("Importing time: %s" % (time.time() - start_time))

print("Start inserting...")
start_time = time.time()
r.eval(script, 300024, *emp_list)
print("[REDIS INSERT BY LUA] Execution time: %s" % (time.time() - start_time))

lua_file.close()

print("--- WORKING ON 2.844.047 RECORDS ---")

lua_file = open("../redis-script/redis_sala_insert.lua", "r")
script = lua_file.read()

manager = mul.Manager()
params_list = manager.list()

salaries = pd.read_csv("../salaries.csv")

def importSala(i):
    params_list.append("emp_no:" + str(salaries['emp_no'][i]) + ":from_date:" + salaries['from_date'][i] +
    ",salary," + str(salaries['salary'][i]) +
    ",to_date," + salaries['to_date'][i])

print("Import data from salaries.csv...")
p = mul.Pool(mul.cpu_count())
start_time = time.time()
p.map(importSala, range(0,2844047))
sala_list = list(params_list)
print("Importing time: %s" % (time.time() - start_time))

print("Start inserting...")
start_time = time.time()
r.eval(script, 700000, *sala_list[:700000])
r.eval(script, 700000, *sala_list[700000:1400000])
r.eval(script, 700000, *sala_list[1400000:2100000])
r.eval(script, 744047, *sala_list[2100000:])
print("[REDIS INSERT BY LUA] Execution time: %s" % (time.time() - start_time))

lua_file.close()