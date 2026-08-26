units = int(input("Enter your units: "))

if units <= 100:
    total = units * 5
elif units <= 200:
    total = ((units - 100) * 7 ) + (100 * 5)
else:
    total = ((units - 200) * 10 ) + (100 * 7) + (100 * 5)

print(f"Your electricity bill is ${total}")
