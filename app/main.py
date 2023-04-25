from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from constants import EXC401
from crud import create, delete, read_list, update
from engine import api
from models import User, Project
from schemas import (ProjectScheme, UserCreateScheme,
                     UserRepresentScheme, UserUpdateScheme)
from utils import auth_user, create_token, get_current_user, get_pass_hash


@api.post('/token')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = auth_user(form.username, form.password)
    if not user:
        raise EXC401
    token = create_token({'sub': user.username})
    return {'Bearer': token}


@api.post('/users', response_model=UserRepresentScheme)
async def create_user(user: UserCreateScheme):
    user.password = get_pass_hash(user.password)
    user_obj = create(User, user.dict())
    return user_obj


@api.get('/users', response_model=list[UserRepresentScheme])
async def get_users(cur_user: User = Depends(get_current_user)):
    """Get all users."""
    return read_list(User)


@api.get('/users/me', response_model=UserRepresentScheme)
async def get_user(cur_user: User = Depends(get_current_user)):
    return cur_user


@api.patch('/users/me', response_model=UserRepresentScheme)
async def update_user(user: UserUpdateScheme,
                      cur_user: User = Depends(get_current_user)):
    if user.password:
        user.password = get_pass_hash(user.password)
    payload = user.dict(exclude_unset=True, exclude_none=True)
    update(User, f'id == {cur_user.id}', payload)
    return user


@api.delete('/users/me')
async def delete_user(cur_user: User = Depends(get_current_user)):
    delete(User, f'id == {cur_user.id}')


@api.post('/projects')
async def add_project(
    proj: ProjectScheme,
    cur_user: UserRepresentScheme = Depends(get_current_user)
):
    return proj
