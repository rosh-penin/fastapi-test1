from pydantic import BaseModel


class ImageCreateScheme(BaseModel):
    filename: str
    bytes: str

    class Config:
        orm_mode = True


class ImageGetScheme(BaseModel):
    id: int
    filename: str
    bytes: str

    class Config:
        orm_mode = True


class ProjectCreateScheme(BaseModel):
    name: str
    images: list[ImageCreateScheme] | None

    class Config:
        orm_mode = True


class ProjectGetScheme(BaseModel):
    name: str
    images: list[ImageGetScheme]

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
