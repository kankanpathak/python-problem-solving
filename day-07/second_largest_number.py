n = int(input("How many numbers: "))

my_list = []

print("Enter numbers: ")

for _ in range(n):
    my_list.append(int(input()))

largest = float("-inf")
second_largest = float("-inf")

for i in my_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i

print(f"Second largest: {second_largest}")
