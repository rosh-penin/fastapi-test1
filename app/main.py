from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from constants import EXC401
from engine import api, Session
from models import User, Project
from schemas import ProjectScheme, UserCreateScheme, UserRepresentScheme
from utils import auth_user, create_token, get_current_user, get_pass_hash


@api.post('/token')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = auth_user(form.username, form.password)
    if not user:
        raise EXC401
    token = create_token({'sub': user.username})
    return {'token': token}


@api.post('/users')
async def create_user(user: UserCreateScheme):
    user.password = get_pass_hash(user.password)
    with Session.begin() as session:
        user_obj = User(**user.dict())
        session.add(user_obj)
        return UserRepresentScheme(user_obj)


# @api.get('/users')
# async def verify_user(user_sc: UserCreateScheme):
#     with Session() as session:
#         user = session.query(User).filter_by(username=user_sc.username).first()
#         return verify_pass(user_sc.password, user.password)


@api.post('/projects')
async def add_project(
    proj: ProjectScheme,
    cur_user: UserRepresentScheme = Depends(get_current_user)
):
    return proj
