def handle_case(item):
    match item:
        case [1, message] if message == "Hello":
            return message
        case [2, message] if message == "World":
            return message
        case [3, message] if message == "Random":
            return message
        case _:
            return "Unknown"

print(handle_case([3, "Random"]))