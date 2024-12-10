from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


@router.get("/")
async def read_root():
    return {"Connected to Backend Service of Alpha"}



@router.get("/health")
async def health():
    return True