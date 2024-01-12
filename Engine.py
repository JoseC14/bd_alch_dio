from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory')


def get_engine():
    global engine
    return engine