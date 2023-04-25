from pydantic import BaseModel


class ImageGetScheme(BaseModel):
    filename: str
    url: str


class ProjectScheme(BaseModel):
    name: str
    images: list[ImageGetScheme] | None


class UserCreateScheme(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
    password: str


class UserRepresentScheme(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str
