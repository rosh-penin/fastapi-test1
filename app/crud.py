from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import Session as sql_session

from constants import EXC404, EXCINT
from engine import Base


def create(session: sql_session, model: Base, payload: dict):
    obj = model(**payload)
    try:
        session.add(obj)
        session.commit()
    except IntegrityError:
        raise EXCINT
    return obj


def delete(session: sql_session, model: Base, lookup_expr: dict):
    """Not really DRY but in one session. Delete obj from db."""
    try:
        obj = session.query(model).filter_by(**lookup_expr).one()
    except NoResultFound:
        raise EXC404
    session.delete(obj)


def read(session: sql_session, model: Base, lookup_expr: dict):
    try:
        obj = session.query(model).filter_by(**lookup_expr).one()
    except NoResultFound:
        raise EXC404
    return obj


def read_list(session: sql_session, model: Base,
              lookup_expr: dict | None = None):
    if not lookup_expr:
        return session.query(model).all()
    return session.query(model).filter_by(**lookup_expr).all()


def update(session: sql_session, model: Base,
           lookup_expr: dict, payload: dict):
    session.query(model).filter(**lookup_expr).update(payload)
    return
