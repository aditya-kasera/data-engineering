
from Connection import get_db
from fastapi import Depends # used for dependency injection
from fastapi import FastAPI # used to create the web application
from sqlalchemy.orm import Session # used for database sessions
# SQLAlchemy - a SQL toolkit and Object-Relational Mapping (ORM)


app = FastAPI()  # creates a FastAPI application instance 

@app.post("/patient") # decorator that defines an HTTP POST endpoint

def add_patient(patient: dict, database_client: Session = Depends(get_db)):
    # (variable: type, Session instance obtained through dependency injection using the Depends)
    patient_collection = database_client["patients"]
    patient_collection.insert_one(patient) # after converting patient obj. -> json obj.
    return "Pateint Added."

@app.post("/patient/{patient_id}") # decorator that defines an HTTP POST endpoint

def add_patient(patient_id: str, database_client: Session = Depends(get_db)):
    
    patient_collection = database_client["patients"]
    patient = patient_collection
    patient_collection.find_one({"_id": ObjectId(patient_id)}) # after converting patient obj. -> json obj.
    patient["_id"] = str(patient["_id"])
    return patient



# {path_variable}
# list comprehension




# uvicorn APIs:app --reload  
# to run






















































































# import requests
# response = requests.get("http://api.open-notify.org/astros") 
# print(response.status_code) # 200
