from pydantic import BaseModel


class ImageGetScheme(BaseModel):
    filename: str
    url: str


class ProjectScheme(BaseModel):
    name: str
    images: list[ImageGetScheme] | None


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
