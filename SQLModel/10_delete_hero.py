from sqlmodel import SQLModel, Field, select, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_url = 'sqlite:///database.db'
engine = create_engine(sqlite_url, echo=True)


def delete_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age < 35)
        results = session.exec(statement)
        hero = results.first()

        print(hero)

        session.delete(hero)
        # session.add()  不需要
        session.commit()
        # session.refresh(hero)  不需要

        print(hero)


def main():
    delete_hero()


if __name__ == '__main__':
    main()
