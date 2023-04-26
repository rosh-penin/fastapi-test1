from sqlalchemy import ForeignKey, select, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property

from engine import Base, engine


class User(Base):
    __tablename__ = 'users_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    projects: Mapped[list['Project']] = relationship(
        back_populates='user',
        lazy='joined',
        cascade='all, delete-orphan'
    )
    projects_count: Mapped[int] = column_property(
        select(func.count('projects_table.id'))
        .where('projects_table.user_id' == id)
    )


class Project(Base):
    __tablename__ = 'projects_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users_table.id'))
    user: Mapped['User'] = relationship(back_populates='projects')
    images: Mapped[list['Image']] = relationship(
        back_populates='project',
        lazy='joined',
        cascade='all, delete-orphan'
    )
    images_count: Mapped[int] = column_property(
        select(func.count('images_table.id'))
        .where('images_table.project_id' == id)
    )


class Image(Base):
    __tablename__ = 'images_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(unique=True)
    bytes: Mapped[str]
    project_id: Mapped[int] = mapped_column(ForeignKey('projects_table.id'))
    project: Mapped['Project'] = relationship(back_populates='images')


Base.metadata.create_all(engine)
