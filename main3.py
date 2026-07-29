from fastapi import FastAPI
import models
from database import engine
from router import blog, user, authentication

app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
