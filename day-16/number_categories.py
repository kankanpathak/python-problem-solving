def get_positive(numbers):
    positive_numbers = []
    for i in numbers:
        if i > 0:
            positive_numbers.append(i)

    return f"Positive: {positive_numbers}"

def get_negative(numbers):
    negative_numbers = []
    for i in numbers:
        if i < 0:
            negative_numbers.append(i)

    return f"Negative: {negative_numbers}"

def count_zeros(numbers):
    count = 0
    for i in numbers:
        if i == 0:
            count += 1

    return f"Zeros: {count}"


numbers = [12, -5, 0, 8, -3, 7, 0, -10, 15]

print(get_positive(numbers))
print(get_negative(numbers))
print(count_zeros(numbers))
