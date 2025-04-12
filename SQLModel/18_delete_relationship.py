from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def delete_relationship():
    with Session(engine) as session:
        hero_spider_boy: Hero = session.exec(select(Hero).where(Hero.name == 'Spider-Boy')).one()

        # 只需将对应的team属性设为None, 就能删除关系,
        # 对应的,表中team_id的值夜会变成null
        hero_spider_boy.team = None

        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)

        print(hero_spider_boy)


def main():
    delete_relationship()


if __name__ == "__main__":
    main()
