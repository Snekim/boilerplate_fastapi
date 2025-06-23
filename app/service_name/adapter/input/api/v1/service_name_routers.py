from fastapi import APIRouter


service_name_router = APIRouter()


@service_name_router.get('/index')
async def index():
    return {'status': "It's ALIVE!"}