import json

# Using raw string literal for file path or escaping backslashes
file_path = r'Assignments\Python Assignment - Use Case\PythonTraining.json'
#raw string literal

with open(file_path, 'r') as read_file:
    data = json.load(read_file)

name = data["name"]
date = data["date"]
completed = data["completed"]
instructor_name = data["instructor"]["name"]
instructor_website = data["instructor"]["website"]
participants = data["participants"]

print("name : ", name)
print("date : ", date)
print("completed : ", completed)
print("instructor name : ", instructor_name)
print("instructor website : ", instructor_website)
print("participants : ")
for p in participants:
    print("name : ", p["name"])
    print("email : ", p["email"])

'''
    OUTPUT 
        PS D:\PROGRAMMING\Python> python -u "d:\PROGRAMMING\Python\Assignments\Python Assignment - Use Case\HandleJSON.py"
        name :  Python Training
        date :  April 19, 2024
        completed :  True
        instructor name :  XYZ
        instructor website :  http://pqr.com/
        participants : 
        name :  Participant 1
        email :  email1@example.com
        name :  Participant 2
        email :  email2@example.com
        PS D:\PROGRAMMING\Python> 
'''

