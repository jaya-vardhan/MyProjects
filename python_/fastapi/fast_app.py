from fastapi import Depends, FastAPI, Request, status, HTTPException
from typing import Optional, Union, List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from database import Base
import time
import asyncio


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True, index=True, nullable=False)
    active = Column(Boolean, default=True)


app = FastAPI()

# Base.metadata.create_all(bind=engine)


class UserData(BaseModel):
    name: str
    age: Optional[Union[int, str]] = 40

class ResponseModel(BaseModel):
    message: str
    success: bool = False

class UserResponseModel(ResponseModel):
    users: UserData

class UsersResponseModel(ResponseModel):
    users: List[UserData]


# class User:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age



@app.get('/')
def get_user_info():
    print("hello /")
    time.sleep(10)
    print("bye /")
    return {
        'message': 'Success',
        'users': [
            {
                'name': 'test'
            }
        ]
    }


# @app.get('/{name}')
# def get_user_info(name):
#     return {
#         'message': 'Success',
#         'users': [
#             {
#                 'name': f'Name res for {name}'
#             }
#         ]
#     }


@app.get('/greet')
def get_user_info(name, age:Optional[int]=8):
    # print("hello")
    # time.sleep(10)
    # print("bye")
    return {
        'message': 'Success',
        'users': [
            {
                'name': f'Greeting for Mr. {name} with {age}'
            }
        ]
    }


# @app.post('/')
@app.api_route('/', methods=['POST'], status_code=status.HTTP_201_CREATED)
def get_user_info(request: Request, data: UserData):
    # print(request)
    # print(await request.body())
    # req = request.json()
    # res = {
    #     'name': data.name,
    #     'age': data.age,
    #     'class': 10
    # }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Byee")
    return {
        'message': 'Success',
        # 'users': [User(name=data.name, age=data.age)]
        'users': [User(**data.model_dump())]
    }


def common_query_params(skip: int = 0, limit: int = 10):
    print("common_query_params")
    return {"skip": skip, "limit": limit}


@app.get("/items/")
def read_items(commons: dict = Depends(common_query_params)):
    print("read_items")
    return commons
