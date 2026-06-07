# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from fastapi import FastAPI

app = FastAPI()

items = [
    {
        "id": 1,
        "name": "Ноутбук",
        "price": 35000
    },
    {
        "id": 2,
        "name": "Мишка",
        "price": 800
    },
    {
        "id": 3,
        "name": "Клавіатура",
        "price": 1500
    },
    {
        "id": 4,
        "name": "Монітор",
        "price": 7000
    }
]


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):

    for item in items:

        if item["id"] == item_id:
            return item

    return {
        "message": "Об'єкт не знайдено"
    }