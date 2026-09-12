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
        if is_prime(i) == True:
            prime_numbers.append(i)

    return prime_numbers

     
numbers = [2, 4, 7, 9, 11, 15, 17, 20, 23]

print(find_primes(numbers))
