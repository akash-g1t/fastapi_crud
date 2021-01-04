from fastapi import APIRouter, Request, Query
from main import templates

from models.users_models import User, User_Pydantic, UserIn_Pydantic

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get('/')
async def users(request: Request):
    return templates.TemplateResponse('index.html', {
        "request": request,
        "for": "users router"
    })


@router.get('/all')
async def get_all_users():
    return await User_Pydantic.from_queryset(User.all())

@router.get("/{user_id}")
async def get_single_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))



@router.post('/create')
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)



@router.put('/update/{user_id}')
async def update_user(user_id: int, user: UserIn_Pydantic):
    await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))
