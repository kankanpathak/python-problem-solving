n = int(input("Enter number of elements: "))

lst = []

print("Enter elements: ")

for _ in range(n):
    lst.append(int(input()))

unique_elements = []
frequency = []

for i in lst:
    if i not in unique_elements:
        unique_elements.append(i)

        count = 0

        for j in lst:
            if j == i:
                count += 1

        frequency.append(count)

print(f"Unique elements: {unique_elements}")
print(f"Frequency: {frequency}")
