from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, col


class Hero(SQLModel, table=True):
    # 因为 id 已经是主键，数据库会自动为其创建一个内部索引
    # 数据库总是自动为主键创建内部索引，因为那是组织、存储和检索数据的主要方式。
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
#
# engine = create_engine(sqlite_url, echo=True)
#
#
# def create_heroes():
#     hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
#     hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#     hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
#     hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
#     hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
#     hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
#     hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)
#
#     with Session(engine) as session:
#         session.add(hero_1)
#         session.add(hero_2)
#         session.add(hero_3)
#         session.add(hero_4)
#         session.add(hero_5)
#         session.add(hero_6)
#         session.add(hero_7)
#
#         session.commit()
#
#
# def select_heroes():
#     with Session(engine) as session:
#         statement = select(Hero).where(col(Hero.age) <= 35)  # 这行与上一行一样的效果
#
#         results = session.exec(statement)
#         for hero in results:
#             print(hero)
#
#
# def main():
#     # create_heroes()
#     select_heroes()
#
#
# if __name__ == "__main__":
#     main()
