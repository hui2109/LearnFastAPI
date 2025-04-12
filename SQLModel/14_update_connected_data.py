from sqlmodel import SQLModel, create_engine, Session, Field, select


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


def update_connect_data():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.team_id == None)
        hero: Hero = session.exec(statement).first()

        statement = select(Team).where(Team.name == 'Preventers')
        team: Team = session.exec(statement).first()

        hero.team_id = team.id

        session.add(hero)
        session.commit()
        session.refresh(hero)

        print(hero)


if __name__ == '__main__':
    update_connect_data()
