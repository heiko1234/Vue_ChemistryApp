
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()

@router.get("/access")
async def access():
    return ["LU_MES", "LA_MES"]


