n = int(input("Enter number of elements: "))

lst = []

print("Enter elements:")

for _ in range(n):
    lst.append(int(input()))

new_lst = []

for i in lst:
    count = 0
    
    for j in lst:
        if i == j:
            count += 1
    if count == 1:
        new_lst.append(i)

print(new_lst)
