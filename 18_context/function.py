import contextlib

@contextlib.contextmanager
def fibo(value: str):
    try:
        print(f"Starting Fibonacci sequence with value: {value}")
        yield value
        print(f"Ending Fibonacci sequence with value: {value}")
    except Exception as e:
        print(f"An exception occurred inside Fibonacci context: {e}")
    finally:
        print(f"Cleaning up Fibonacci sequence with value: {value}")

with fibo("Fibonacci") as fibo_value:
    print(f"Inside context with value: {fibo_value}")
    # Uncomment the next line to see exception handling in action
    raise ValueError("An error occurred inside the Fibonacci context")

print("Outside the Fibonacci context")