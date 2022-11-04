from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from routers.schemas import PostBase, PostDisplay

from database.database import get_db
from database import database_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return database_post.create(db, request)