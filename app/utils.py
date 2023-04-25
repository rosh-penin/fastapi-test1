from datetime import datetime, timedelta

from fastapi import Depends
from jose import JWTError, jwt

from constants import (ALGORITHM, EXC401, OAUTH2_SCHEME, PWD_CONTEXT,
                       SECRET_KEY, TOKEN_EXP_MIN)
from crud import read
from models import User


def auth_user(username: str, password: str):
    user_obj = read(User, {'username': username})
    if not user_obj:
        return False
    if not verify_pass(password, user_obj.password):
        return False
    return user_obj


def create_token(data: dict, expires_d: timedelta = TOKEN_EXP_MIN):
    expires = datetime.utcnow() + expires_d
    data.update({'exp': expires})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(OAUTH2_SCHEME)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if not username:
            raise EXC401
    except JWTError:
        raise EXC401
    user = read(User, {'username': username})
    if user is None:
        raise EXC401
    return user


def get_pass_hash(password: str):
    return PWD_CONTEXT.hash(password)


def verify_pass(password: str, hashed_password: str):
    return PWD_CONTEXT.verify(password, hashed_password)
