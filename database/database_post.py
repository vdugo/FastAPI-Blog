import datetime

from fastapi import HTTPException, status

from database.models import DbPost
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session

def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(DbPost).all()

def delete_post(id: int, db: Session):
    post_to_delete = db.query(DbPost).filter(DbPost.id == id).first()
    if not post_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exist.')
    db.delete(post_to_delete)
    db.commit()
    return f'Post with id {id} deleted.'