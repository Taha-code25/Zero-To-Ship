from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.post import PostCreate, PostUpdate, PostOut
from app.models.post import TradePost
from app.models.user import User
from app.dependencies.auth import get_current_user
from app.database import get_all_posts, save_all_posts, get_next_post_id

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("", response_model=List[PostOut])
def list_posts():
    posts = get_all_posts()
    return list(posts.values())


@router.post("", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(body: PostCreate, current_user: User = Depends(get_current_user)):
    posts = get_all_posts()
    pid = get_next_post_id()
    post = TradePost(
        post_id=pid,
        title=body.title,
        description=body.description,
        owner_id=current_user.id,
        status=body.status or "Open",
    )
    posts[pid] = post
    save_all_posts(posts)
    return post


@router.put("/{post_id}", response_model=PostOut)
def update_post(
    post_id: int,
    body: PostUpdate,
    current_user: User = Depends(get_current_user),
):
    posts = get_all_posts()
    post = posts.get(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only edit your own posts",
        )

    if body.title is not None:
        post.title = body.title
    if body.description is not None:
        post.description = body.description
    if body.status is not None:
        post.status = body.status

    posts[post_id] = post
    save_all_posts(posts)
    return post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    current_user: User = Depends(get_current_user),
):
    posts = get_all_posts()
    post = posts.get(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own posts",
        )

    del posts[post_id]
    save_all_posts(posts)
