n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    reverse = n % 10 + reverse * 10
    n = n // 10

print(f"Reverse: {reverse}")
