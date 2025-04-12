from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, col


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()


def select_heroes():
    with Session(engine) as session:
        statement1 = select(Hero).where(Hero.age >= 35).where(Hero.age < 40)
        statement2 = select(Hero).where(Hero.age >= 35, Hero.age < 40)  # 这行与上一行一样的效果
        statement3 = select(Hero).where(or_(Hero.age <= 35, Hero.age > 90))
        statement4 = select(Hero).where(col(Hero.age) <= 35)  # 这行与上一行一样的效果
        # 这是因为我们使用的是纯 Python 注解字段， age 确实被注解为 int | None (or Optional[int])
        # 我们可以告诉编辑器，这个类属性实际上是一个特殊的 SQLModel 列（而不是一个具有正常值的实例属性）
        # 为此，我们可以导入 col() （作为“列”的简称）

        # SELECT 用于告诉 SQL 数据库返回哪些列
        # WHERE 用于告诉 SQL数据库返回哪些行

        results = session.exec(statement4)
        for hero in results:
            print(hero)


def main():
    create_heroes()
    select_heroes()


if __name__ == "__main__":
    main()
