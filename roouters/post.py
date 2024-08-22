from fastapi import APIRouter, Depends, HTTPException, status

from schemas import Postschemas, post
from models.post import Postmodel
import main

router = APIRouter(
    tags=["Post"],
)


@router.post('/userpost')
def create_user(post: Postschemas):
    main.cursor.execute("INSERT INTO post (id, title, content, published) VALUES (%s, %s, %s, %s) RETURNING *",
                   (post.id, post.title, post.content, post.published))
    posts = main.cursor.fetchone()

    main.conn.commit()
    return posts

@router.get('/post')
def get_posts():
    main.cursor.execute("SELECT * FROM post ORDER BY id LIMIT 1 OFFSET 2")
    post = main.cursor.fetchall()
    return post

@router.put('/userpost/{post_id}')
def create_user(post: Postschemas, post_id: int):
    main.cursor.execute("UPDATE post SET  id = %s, title = %s, content = %s, published = %s WHERE  id = %s RETURNING *",
                        (post.id, post.title, post.content, post.published, post_id))

    posts = main.cursor.fetchone()
    main.conn.commit()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This post not exist')
    return {'details': posts}


@router.get('/getpost/id')
def get_post(id: int):
    main.cursor.execute("SELECT * FROM post WHERE id = %s", (id,))
    posts = main.cursor.fetchone()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with this id {id} does not exist")
    return {"post_details": posts}

@router.delete('/deletepost/{post_id}')
def delete_post(post_id: int):
    main.cursor.execute("DELETE FROM post WHERE id = %s returing *", (post_id,))
    posts = main.conn.commit()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found or already deleted")

    return {"detail": f"Post with id {post_id} has been deleted"}