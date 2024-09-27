from sqlmodel import create_engine, Session, SQLModel
from settings import env_store

database_url = env_store.DATABASE_URL
print(f"-----${database_url}-----")

engine = create_engine(database_url)


async def get_db_connection():
    try:
        session = Session(engine)
        yield session
    finally:
        session.close()


def init_db():
    SQLModel.metadata.create_all(engine)
