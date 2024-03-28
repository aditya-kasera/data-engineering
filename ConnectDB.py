# pip install my-sql-connector-python
# create a connection obj
import mysql.connector as mc
con_obj = mc.connect(host="localhost", user="root", passwd="grassroot")
print(con_obj)

cur_obj = con_obj.cursor()
print(cur_obj)
try:
    # cur_obj.execute("CREATE DATABASE PYTHON_DB")
    cur_obj.execute("SHOW DATABASES")
except:
    con_obj.rollback()

for x in cur_obj:
    print(x)

con_obj.close()
    