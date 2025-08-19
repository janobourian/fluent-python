class SimpleContextManager:
    def __init__(self):
        print("Initializing SimpleContextManager")
        pass
    
    def __enter__(self):
        print(f"Entering context")
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        print("Exiting context")
        return False

with SimpleContextManager() as cm:
    print("Inside the context")
    # Uncomment the next line to see exception handling in action
    # raise ValueError("An error occurred inside the context")
    
print("Outside the context")