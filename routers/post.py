import shutil
import string
import random

from fastapi import APIRouter, Depends, File, UploadFile
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

@router.post('/image')
def upload_image(image: UploadFile = File(...), ):
    letters = string.ascii_letters
    rand_str = ' '.join(random.choice(letters) for i in range(6))
    new_image = f'_{rand_str}.'
    filename = new_image.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"filename": path}
        
    
@router.get('/all')
def get_all_posts(db: Session = Depends(get_db)):
    return database_post.get_all_posts(db)

@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    return database_post.delete_post(id, db)