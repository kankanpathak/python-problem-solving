n = int(input("How many numbers: "))

my_list = []

print("Enter numbers: ")

for _ in range(n):
    my_list.append(int(input()))

k = int(input("Enter value of k: "))

k = k % len(my_list)

new_list = []

for i in range(k):
    for j in range(len(my_list)-1, -1, -1):
        new_list.insert(0, my_list[j])
        my_list.remove(my_list[j])
        break

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
