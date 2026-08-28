n = int(input("Enter a number: "))

count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        r = n % 10
        n = n // 10
        count += 1
    
print(f"Digits: {count}")
