from fastapi import FastAPI

# from app import models
# from app.database import engine
# from app.routers.users import users_router
# from app.routers.records import records_router
# models.Base.metadata.create_all(bind=engine)

import models
from database import engine
from routers.users import users_router
from routers.records import records_router
from routers.mlrouter import ml_router
models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users_router)
app.include_router(records_router)
app.include_router(ml_router)