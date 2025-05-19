from fastapi import FastAPI

import models
import database
from routers import products, benefits, conditionaloffers, basket

app = FastAPI()

app.include_router(products.router)
app.include_router(benefits.router)
app.include_router(conditionaloffers.router)
app.include_router(basket.router)

# database.Base.metadata.create_all(database.engine) # only use this when you want SQLalchemy to create all initial schemas
