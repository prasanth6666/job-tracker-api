from fastapi import APIRouter
router = APIRouter(prefix = "/jobs",tags =["jobs"])

@router.get("/")
def get_jobs():
    return [
        {"id":1,"title":"software engineer"},
        {"id":2,"title":"data scientist"}
    ]
