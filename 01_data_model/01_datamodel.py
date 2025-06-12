information = {
    "name": "Data Model",
    "description": "This module defines the data model for the application.",
    "version": "1.0",
}

print(information.__getitem__("name"))


def get_item(data: dict, key: str):
    return data.__getitem__(key)


print(get_item(information, "version"))


class Printer:

    def __supply__(self):
        return "supply"


printer = Printer()
print(printer.__supply__())
