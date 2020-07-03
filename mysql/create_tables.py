import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hoangvanhieu",
  database="testdb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_no INT PRIMARY KEY, birth_date DATE, first_name VARCHAR(14), last_name VARCHAR(16), gender ENUM('M','F'), hire_date DATE)")
mycursor.execute("CREATE TABLE IF NOT EXISTS salaries (emp_no INT, from_date DATE, salary INT, to_date DATE, PRIMARY KEY (emp_no, from_date))")

print("Tables created.")