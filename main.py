from typing import Dict, Union, List, Annotated, Optional

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, EmailStr, Field
import uvicorn
from models import User

app = FastAPI()
default_db: List[User] = []

@app.get("/users/", response_model=User)
def get_emailuser(email: EmailStr = Query(...,description="Електронна пошта.")):
    for user in default_db:
        if user.email == email:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Користувача не знайдено.")


@app.post("/users/")
def user_created(user: User):
    for ex_user in default_db:
        if ex_user.email == user.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Користувача з такою електронною поштою не знайдено.")
    default_db.append(user)
    return "Користувача додано."
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)