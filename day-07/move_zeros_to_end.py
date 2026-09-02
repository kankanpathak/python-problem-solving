n = int(input("How many numbers: "))

my_list = []

print("Enter numbers: ")

for _ in range(n):
    my_list.append(int(input()))

new_list = []

for i in my_list:
    if i != 0:
        new_list.append(i)

for i in my_list:
    if i == 0:
        new_list.append(i)

print(f"Output: {new_list}")
