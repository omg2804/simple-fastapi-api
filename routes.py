from fastapi import APIRouter
from main import read_root

router = APIRouter()

router.get("/")
async def root():
    return await read_root()