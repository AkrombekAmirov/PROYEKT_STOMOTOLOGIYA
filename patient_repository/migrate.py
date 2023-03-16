from sqlmodel import SQLModel


def migrate(engine):
    SQLModel.metadata.create_all(engine)


def unmigrate(engine):
    SQLModel.metadata.drop_all(engine)


def remigrate(engine):
    unmigrate(engine)
    migrate(engine)
