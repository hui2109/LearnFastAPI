from sqlmodel import SQLModel, Field, select, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_url = 'sqlite:///database.db'
engine = create_engine(sqlite_url, echo=True)


def select_with_offset_limit():
    with Session(engine) as session:
        statement = select(Hero).offset(1).limit(2)
        results = session.exec(statement)
        for hero in results:
            print(hero)


def main():
    select_with_offset_limit()


if __name__ == '__main__':
    main()
