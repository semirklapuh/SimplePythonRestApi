from telnetlib import STATUS
from this import d
from uuid import UUID
from fastapi import FastAPI, HTTPException
from typing import List

from models import Gender, Role, User, UserUpdate

app = FastAPI()


db: List[User] = [
    User(id=UUID("49c7a446-9352-4f4b-8e99-a147f518d98e"), first_name="Semir",middle_name="Sema" ,last_name="Klapuh", gender=Gender.male, roles=[Role.admin]),
    User(id=UUID("1b7c40dd-d234-4bd2-9d0d-894d07b7581c"), first_name="Amina", last_name="Ami", gender=Gender.female, roles=[Role.student, Role.user])
]
 

@app.get("/api/v1/users")
def getAllUsers():
    return db

@app.post("/api/v1/users")
def insertUser(user: User):
    db.append(user)
    return {"UUID": user.id}


@app.delete("/api/v1/users/{user_id}")
def DeleteUser(user_id: UUID):
        for user in db:
            if user.id == user_id:
                db.remove(user)
                return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )

@app.put("/api/v1/users")
def UpdateUser(userUpdate: UserUpdate):
    for user in db:
        if user.id == userUpdate.id:
            if userUpdate.first_name != None:
             user.first_name = userUpdate.first_name
            if userUpdate.last_name != None:
             user.last_name = userUpdate.last_name
            if userUpdate.middle_name != None:
             user.middle_name = userUpdate.middle_name
            if userUpdate.roles != None:
             user.roles = userUpdate.roles
            return user


    #user = next((x for x in db if x.id == userUpdate.id), None)
    #return user
   