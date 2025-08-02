number_1 = 5
number_2 = 10
result = lambda number_1, number_2 : number_1 + number_2
print(f"The sum of {number_1} and {number_2} is: {result(number_1, number_2)}")

lambda_function = [ (lambda x: x**2)(x) for x in range(5) ]
print(lambda_function)