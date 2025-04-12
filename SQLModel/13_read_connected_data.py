from sqlmodel import Field, Session, SQLModel, create_engine, select


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def select_heroes():
    with Session(engine) as session:
        # select使用了两个类Hero 和 Team
        statement = select(Hero, Team).where(Hero.team_id == Team.id)

        # 使用join, 也可以达到相同的效果
        statement = select(Hero, Team).join(Team)

        # .join() 有一个参数我们可以使用 isouter=True 来使 JOIN 成为 LEFT OUTER JOIN
        statement = select(Hero, Team).join(Team, isouter=True)

        # Select Only Heroes But Join with Teams
        # 如果我们只把 Team 放在 .join() 中，而不是放在 select() 函数中，我们就不会得到 team 的数据。
        statement = select(Hero).join(Team).where(Team.name == "Preventers")

        results = session.exec(statement)
        # for hero, team in results:
        #     print("Hero:", hero, "Team:", team)

        for hero in results:
            print("Hero:", hero)


def main():
    select_heroes()


if __name__ == "__main__":
    main()
