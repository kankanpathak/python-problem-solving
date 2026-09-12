def find_even_numbers(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)

    return even_numbers

def find_odd_numbers(numbers):
    odd_numbers = []
    for i in numbers:
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers

def calculate_average(numbers):
    total = 0
    count = 0
    for i in numbers:
        total += i
        count += 1

    return round((total / count), 2)

def analyze_numbers(numbers):
    return f"Even: {find_even_numbers(numbers)}\nOdd: {find_odd_numbers(numbers)}\nAverage: {calculate_average(numbers)}"


numbers = [12, 7, 4, 9, 16, 21, 8, 5, 10]

print(analyze_numbers(numbers))
