from pydantic import BaseModel, ConfigDict

class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class SimpleUser(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class ShowBlog(Blog):
    user: SimpleUser

    model_config = ConfigDict(from_attributes=True)


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []

    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None