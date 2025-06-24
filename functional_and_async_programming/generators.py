line_list = ['  line 1\n', 'line 2  \n', ' \n', '']

# Generators are a special kind of iterator
stripped_iter = (line.strip() for line in line_list)
print(stripped_iter)

# List comprehension
stripped_list = [line.strip() for line in line_list]
print(stripped_list)

# With if
stripped_list = [line.strip() for line in line_list if line != ""]
print(stripped_list)

# Generator functions is not destroyed when it is called
def generate_ints(N):
    for i in range(N):
        yield i