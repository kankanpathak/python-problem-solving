n = int(input("How many numbers: "))

my_list = []

print("Enter numbers: ")

for _ in range(n):
    my_list.append(int(input()))

largest = float("-inf")

for i in my_list:
    if i > largest:
        largest = i

print(f"Largest: {largest}")
