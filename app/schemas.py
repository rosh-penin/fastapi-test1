from pydantic import BaseModel


class ImageGetScheme(BaseModel):
    filename: str
    url: str

    class Config:
        orm_mode = True


class ImageCreateScheme(BaseModel):
    filename: str
    bytes: str


class ProjectCreateScheme(BaseModel):
    name: str
    images: list[ImageCreateScheme] | None
    user_id: str | None

    class Config:
        orm_mode = True


class UserRepresentScheme(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str

    class Config:
        orm_mode = True


class UserCreateScheme(UserRepresentScheme):
    password: str


class UserUpdateScheme(UserRepresentScheme):
    username: str | None
    password: str | None
