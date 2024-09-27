from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from contextlib import asynccontextmanager
from db.config import get_db_connection, init_db
from sqlmodel import SQLModel, Session, select
from db.models import link
from settings import env_store


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("---app starting---")
    init_db()
    yield
    print("---app closing---")


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    print(env_store.DATABASE_URL)
    return "Welcome to the api"


@app.post("/links/{title}")
async def add_link(title: str, db: Annotated[Session, Depends(get_db_connection)]):
    try:
        new_link = link.Link(title=title)
        print(new_link)
        db.add(new_link)
        db.commit()

        return new_link
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong when creating the link",
        )


@app.get("/links")
async def get_links(db: Annotated[Session, Depends(get_db_connection)]):
    try:
        statement = select(link.Link)
        results = db.exec(statement)

        return results.all()
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong when fetching the links",
        )
