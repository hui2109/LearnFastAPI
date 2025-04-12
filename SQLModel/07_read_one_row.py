from sqlmodel import SQLModel, Field, Session, select, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def select_one_row():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age <= 35)  # 这行与上一行一样的效果
        results = session.exec(statement)

        # 这将返回 results 中的第一个对象（如果有的话）
        # 可能 SQL 查询找不到任何行, 在这种情况下， .first() 将返回 None
        hero = results.first()

        # 有可能我们想要确保查询结果恰好有一行; 如果有多个，则意味着系统中存在错误，我们应该终止并报错
        # 在这种情况下，我们可以使用 .one() 代替 .first()
        # hero = results.one()

        # Select by Id with .where()
        statement = select(Hero).where(Hero.id == 1)
        results = session.exec(statement)
        hero = results.first()

        # 选择通过主键的 ID 列选择单行是一个常见操作，因此有一个快捷方式：
        hero = session.get(Hero, 1)

        print(hero, type(hero))


def main():
    select_one_row()


if __name__ == '__main__':
    main()
