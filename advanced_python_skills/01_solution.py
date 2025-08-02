# Summing numbers like in school
from itertools import zip_longest

def sum_numbers(number_1, number_2, base):
    first_value = str(number_1)[::-1]
    second_value = str(number_2)[::-1]
    zipped_values = list(zip_longest(first_value, second_value, fillvalue='0'))    
    print("Zipped values:", zipped_values)
    temp_results = []
    for first, second in zipped_values:
        temp_results.append([
            (int(first) + int(second)) % base,
            (int(first) + int(second)) // base
        ])
    print(f"Temporary results before base conversion: {temp_results}")
    final_result = []
    for i in range(len(temp_results)):
        if i == 0:
            final_result.append(temp_results[i][0])
        else:
            final_result.append((temp_results[i][0] + temp_results[i-1][1]))
    
    final_result.append(0)
    print(f"Final result before base conversion: {final_result}")
    
    for i in range(len(final_result)-1):
        
        if final_result[i] >= base:
            print(f"i: {i}, value: {final_result[i]}")
            temp_value = final_result[i]
            final_result[i] = temp_value % base
            final_result[i+1] += temp_value // base
    
    print(f"Final result after base conversion: {final_result}")
    
    return ''.join(str(x) for x in final_result[::-1]).lstrip('0') or '0'
    
    

if __name__ == "__main__":
    number_1 = 92345
    number_2 = 9789
    base = 10
    result = sum_numbers(number_1, number_2, base)
    print(f"The sum of {number_1} and {number_2} in base {base} is: {result}")