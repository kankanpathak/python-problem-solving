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

def calculate_average(numbers):
    total = 0
    count = 0
    for i in numbers:
        total += i
        count += 1

    return total / count

numbers = [12, 5, 8, 21, 16, 7, 30]

print(find_even_numbers(numbers))
print(find_largest(numbers))
print(calculate_average(numbers))
