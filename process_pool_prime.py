from concurrent.futures import ProcessPoolExecutor
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = [112272535095293, 112582705942171, 115280095190773]

with ProcessPoolExecutor() as executor:
    results = list(executor.map(is_prime, numbers))

for n, r in zip(numbers, results):
    print(n, "is prime:", r)
