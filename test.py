def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


#
#
# print(get_full_name("john", "doe"))
#
#
# def process_items(items: list[str]):
#     for item in items:
#         print(item)
#
#
# def process_items2(items_t: tuple[int, int, str], items_s: set[bytes]):
#     return items_t, items_s
#
#
# def process_items3(prices: dict[str, float]):
#     for item_name, item_price in prices.items():
#         print(item_name)
#         print(item_price)
#
#
# class Person:
#     def __init__(self, name: str):
#         self.name = name
#
#
# def get_person_name(person: Person):
#     return person.name
#
#
# def process_item(item: int | str):
#     print(item)
#
#
# def say_hi(name: str | None = None):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")


from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123


from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


def get_full_name2(first_name: Annotated[str, "this is just metadata"], last_name: Annotated[str, "this is just metadata"]) -> Annotated[str, "this is just metadata"]:
    full_name = first_name.title() + " " + last_name.title()
    return full_name
