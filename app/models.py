from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from engine import Base, engine


class User(Base):
    __tablename__ = 'users_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    projects: Mapped[list['Project']] = relationship(back_populates='user',
                                                     lazy='joined')


class Project(Base):
    __tablename__ = 'projects_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users_table.id'))
    user: Mapped['User'] = relationship(back_populates='projects')
    images: Mapped[list['Image']] = relationship(back_populates='project',
                                                 lazy='joined')


class Image(Base):
    __tablename__ = 'images_table'
    url: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(unique=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects_table.id'))
    project: Mapped['Project'] = relationship(back_populates='images')


Base.metadata.create_all(engine)
