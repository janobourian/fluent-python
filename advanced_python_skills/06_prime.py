def prime_numbers():
    total_prime_numbers = [2]
    current_evaluated = 2
    if current_evaluated == 2:
        current_evaluated += 1
        yield total_prime_numbers[-1]
    while True:
        candidate = current_evaluated
        is_prime = True
        for prime in total_prime_numbers:
            if candidate % prime == 0:
                is_prime = False
                current_evaluated += 1
                break
        if is_prime:
            total_prime_numbers.append(candidate)
            current_evaluated += 1
            yield candidate

gen_prime = prime_numbers()
print(f"One prime number: {next(gen_prime)}")
print(f"One prime number: {next(gen_prime)}")
print(f"One prime number: {next(gen_prime)}")
print(f"One prime number: {next(gen_prime)}")
print(f"One prime number: {next(gen_prime)}")
print(f"One prime number: {next(gen_prime)}")