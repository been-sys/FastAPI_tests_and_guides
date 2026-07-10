from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ConfigDict, # по умолчанию pydantic позволяет передавать на вход новые параметры, однако это можно исправить с помощью ConfigDict
)  # Field испольлзуется для более жесткой валидации

from fastapi import FastAPI

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": None,
    "age": 12,
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10) # ограничение на длину строки

    model_config=ConfigDict(extra='forbid')# запрет на дополнительные параметры

users=[]

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "msg": "Юзер добавлен"}

@app.get("/users")
def get_users(user: UserSchema):
    return users


# в pydantic существует возможность наследования схем
class UserSchema_age_schema(UserSchema):
    age: int = Field(ge=0, le=130)  # greater or equal



# **data означает распаковку элемнтов слова и передача их в виде аргументов
# с соответсвующими именами: "name":"artem" -> name="artem"
def func(data: dict):
    data["age"] += 1
