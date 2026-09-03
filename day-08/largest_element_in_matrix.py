num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

largest = float("-inf")

for i in matrix:
    for j in i:
        if j > largest:
            largest = j

print(f"Largest: {largest}")
