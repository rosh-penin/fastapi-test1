from datetime import timedelta
import os

from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

SECRET_KEY = os.getenv(
    'SECRET',
    '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
)
ALGORITHM = os.getenv('ALGORITHM', "HS256")
TOKEN_EXP_MIN = timedelta(minutes=30)
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='token')
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

EXC400 = HTTPException(400, 'Something gone wrong.')
EXCINT = HTTPException(400, 'Already exists.')
EXC401 = HTTPException(401, 'Imposter!')
EXC404 = HTTPException(404, 'Not found')
