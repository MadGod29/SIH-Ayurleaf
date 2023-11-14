from fastapi import FastAPI
import models,database
import FastAPI_backend.routers.user as user
import FastAPI_backend.routers.auth as auth

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)