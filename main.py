from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from tortoise.contrib.fastapi import register_tortoise

from typing import Optional

# Initializing APP
app = FastAPI()

# Mounting Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Defining templating Engine to Use
templates = Jinja2Templates(directory="templates")


# Registering Tortoise Models
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    # db_url="postgres://test:1234@localhost:5432/fastapi",
    modules={"models": ["models.users_models"]},
    generate_schemas=True,
    add_exception_handlers=True
)




# Including routers
from routers import items, users

app.include_router(items.router)
app.include_router(users.router)