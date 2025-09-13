import array
import timeit

array_to_test = [i for i in range(1000000)]

my_integers = array.array('i', [1, 2, 3, 4, 5])
print(my_integers)

setup = '''
import array
array_to_test = [i for i in range(1000000)]
my_integers = array.array('i', array_to_test)

def power(x: int) -> int:
    return x * x

def operation(values: list[int] | array.array) -> int:
    return sum(map(power, values))
'''

stmt_array = '''
operation(array_to_test)
'''

stmt_list = '''
operation(my_integers)
'''

time_array = timeit.repeat(stmt_array, setup, number=1000, repeat=10)
time_list = timeit.repeat(stmt_list, setup, number=1000, repeat=10)

print(f"Array time: {min(time_array)} - {max(time_array)}")
print(f"List time: {min(time_list)} - {max(time_list)}")