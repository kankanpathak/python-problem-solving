def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
                    
    return True


def find_primes(numbers):
    prime_numbers = []

    for i in numbers:
        if is_prime(i):
            prime_numbers.append(i)

    return prime_numbers


def find_even_numbers(numbers):
    even_numbers = []

    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers


def find_largest(numbers):
    largest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest


def analyze(numbers):
    return f"Primes: {find_primes(numbers)}\nEven numbers: {find_even_numbers(numbers)}\nLargest: {find_largest(numbers)}"


numbers = [12, 7, 4, 9, 16, 21, 8, 5, 10, 13, 20]

print(analyze(numbers))
