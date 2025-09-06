import timeit
import functools

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_optimized(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

def unique_count(nums):
    seen = []
    for num in nums:
        if num not in seen:
            seen.append(num)
    return len(seen)

def unique_count_optimized(nums):
    return len(set(nums))

def first_geq(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def first_geq_optimized(a, x):
    from bisect import bisect_left
    return bisect_left(a, x)

@functools.cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_optimized(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

NUMBER = 1000
REPEAT = 3

print("Two Sum:")
print(timeit.repeat(lambda: two_sum(list(range(100)), 150), number=NUMBER, repeat=REPEAT))
print(timeit.repeat(lambda: two_sum_optimized(list(range(100)), 150), number=NUMBER, repeat=REPEAT))

print("Unique Count:")
print(timeit.repeat(lambda: unique_count(list(range(100))), number=NUMBER, repeat=REPEAT))
print(timeit.repeat(lambda: unique_count_optimized(list(range(100))), number=NUMBER, repeat=REPEAT))

print("First GEQ:")
print(timeit.repeat(lambda: first_geq(list(range(100)), 50), number=NUMBER, repeat=REPEAT))
print(timeit.repeat(lambda: first_geq_optimized(list(range(100)), 50), number=NUMBER, repeat=REPEAT))

print("Fibonacci:")
print(timeit.repeat(lambda: fib(20), number=NUMBER, repeat=REPEAT))
print(timeit.repeat(lambda: fib_optimized(20), number=NUMBER, repeat=REPEAT))