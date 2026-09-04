num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

print("Enter elements: ")

matrix = []

for i in range(num_of_rows):
    lst = []
    for j in range(num_of_elements):
        lst.append(int(input()))
    matrix.append(lst)

even_numbers = 0
odd_numbers = 0

for i in matrix:
    for j in i:
        if j % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
