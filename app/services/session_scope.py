# app/services/session_scope.py

from contextlib import contextmanager

@contextmanager
def session_scope():
    from app import db

    session = db.session
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise