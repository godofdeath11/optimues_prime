import time


def cpu_prime(limit):
    start = time.time()
    not_prime_numbers = set()
    prime_numbers = list()
    for x in range(2, limit):
        for y in range(2, limit):
            if y % x == 0 and y != x:
                not_prime_numbers.add(y)
    for x in range(2, limit):
        if x not in not_prime_numbers:
            prime_numbers.append(x)
    end = time.time()
    print("The process took " + str(end - start) + "second")
    return prime_numbers


def memory_prime(limit):
    start = time.time()
    not_prime_numbers = []
    prime_numbers = []
    for x in range(2, limit):
        for y in range(2, limit):
            not_prime_numbers.append(x * y)
    for x in range(2, limit):
        if x not in not_prime_numbers:
            prime_numbers.append(x)
    end = time.time()
    print("The process took " + str(end - start) + "second")
    return prime_numbers

print(cpu_prime(1000))
print(memory_prime(1000))
    
