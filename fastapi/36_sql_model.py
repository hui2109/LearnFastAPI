from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


# table=True tells SQLModel that this is a table model,
# it should represent a table in the SQL database,
# it's not just a data model (as would be any other regular Pydantic class).
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # Field(index=True) tells SQLModel that it should create a SQL index for this column,
    # that would allow faster lookups in the database when reading data filtered by this column.
    name: str = Field(index=True)

    age: int | None = Field(default=None, index=True)
    secret_name: str


sqlite_file_name = "mydatabase.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Using check_same_thread=False allows FastAPI to use the same SQLite database in different threads.
# This is necessary as one single request could use more than one thread (for example in dependencies).
connect_args = {"check_same_thread": False}

# A SQLModel engine (underneath it's actually a SQLAlchemy engine) is what holds the connections to the database.
# You would have one single engine object for all your code to connect to the same database.
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    # create the tables for all the table models
    SQLModel.metadata.create_all(engine)


# A Session is what stores the objects in memory and
# keeps track of any changes needed in the data, then it uses the [engine] to communicate with the database.
def get_session():
    with Session(engine) as session:
        # We will create a FastAPI dependency with yield that
        # will provide a new Session for each request.
        # This is what ensures that we use a single session per request.
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


# We will create the database tables when the application starts.
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


@app.get("/heroes/")
def read_heroes(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
