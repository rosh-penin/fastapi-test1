from sqlalchemy import text
from sqlalchemy.exc import NoResultFound

from constants import EXC404
from engine import Session, Base


def create(model: Base, payload: dict):
    with Session.begin() as session:
        obj = model(**payload)
        session.add(obj)
        return obj


def delete(model: Base, lookup_expr: dict):
    """Not really DRY but in one session. Delete obj from db."""
    with Session.begin() as session:
        try:
            obj = session.query(model).filter_by(text(lookup_expr)).one()
        except NoResultFound:
            raise EXC404
        session.delete(obj)


def read(model: Base, lookup_expr: dict):
    with Session() as session:
        try:
            obj = session.query(model).filter_by(text(lookup_expr)).one()
        except NoResultFound:
            raise EXC404
        return obj


def read_list(model: Base, lookup_expr: dict | None = None):
    with Session() as session:
        if not lookup_expr:
            return session.query(model).all()
        return session.query(model).filter_by(text(lookup_expr)).all()


def update(model: Base, lookup_expr: str, payload: dict):
    with Session.begin() as session:
        session.query(model).filter(text(lookup_expr)).update(payload)
        return
