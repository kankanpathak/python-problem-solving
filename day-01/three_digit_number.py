num = 583

r1 = num % 10
num = num // 10

r2 = num % 10
num = num // 10

r3 = num % 10

print(f"First digit: {r3}")
print(f"Middle digit: {r2}")
print(f"Last digit: {r1}")
