from fastapi import APIRouter, Request, Query
from main import templates

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get('/')
async def items(request: Request):
    return templates.TemplateResponse('index.html', {
        "request": request,
        "for": "items router"
    })

@router.put('/{item_id}')
async def item(item_id: int, q: str = Query(None, min_length=5, max_length=50)):
    return {
        "Item": f"You item is {item_id}",
        "query": q
    }