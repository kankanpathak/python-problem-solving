n = int(input("How many numbers: "))

original_list = []

print("Enter numbers: ")

for _ in range(n):
    original_list.append(int(input()))

new_list = []

for i in original_list:
    if i not in new_list:
        new_list.append(i)

print(f"Output: {new_list}")
