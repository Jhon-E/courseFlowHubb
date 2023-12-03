from fastapi import FastAPI
from sql import models
from sql.database import engine
from routers.create import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router=router)

