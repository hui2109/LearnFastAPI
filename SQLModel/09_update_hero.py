from sqlmodel import SQLModel, Field, select, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_url = 'sqlite:///database.db'
engine = create_engine(sqlite_url, echo=True)


def update_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age < 35)
        results = session.exec(statement)
        hero = results.first()

        # 更新第一个hero的age值
        print(hero)

        hero.age = 40

        # 三件套: add commit refresh
        session.add(hero)
        session.commit()
        session.refresh(hero)

        print(hero)


def main():
    update_hero()


if __name__ == '__main__':
    main()
