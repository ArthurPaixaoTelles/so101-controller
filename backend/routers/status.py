from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def get_status():
    return{
        "status": "online",
        "version": "1.0.0",
        "docs": "http://localhost:8000/docs",
        "robot": "SO-101"
    }