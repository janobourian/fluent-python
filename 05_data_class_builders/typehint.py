username: str
username = input("Enter your username: ")
print(f"Hello, {username}!")
print(f"Your username is {len(username)} characters long.")

class DemoPlainClass:
    a: int
    b: float = 1.1
    c = "Hello"

print(DemoPlainClass.__annotations__)
print(DemoPlainClass.__doc__)