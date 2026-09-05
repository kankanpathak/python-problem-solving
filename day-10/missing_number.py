n = int(input("Enter n: "))

lst1 = []

expected_total = 0

for i in range(1, n+1):
    lst1.append(i)
    expected_total += i

lst2 = []

print("Enter elements: ")

for i in range(n-1):
    lst2.append(int(input()))

actual_total = 0

for i in lst2:
    actual_total += i

missing_number = expected_total - actual_total

print(f"Missing number is {missing_number}")
