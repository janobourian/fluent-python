import sys

class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
    
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is not None:
            sys.stdout.write(f"An exception occurred: {exc_value}\n")
        return False

with LookingGlass() as what:
    print(what)
    print("Inside the looking glass")
    # Uncomment the next line to see exception handling in action
    # raise ValueError("An error occurred inside the looking glass")

print("Outside the looking glass")