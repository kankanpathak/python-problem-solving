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
current_row = 0
row = 0

for i in matrix:
    temp_even_numbers = 0
    for j in i:
        if j % 2 == 0:
            temp_even_numbers += 1
    current_row += 1
    if temp_even_numbers > even_numbers:
        even_numbers = temp_even_numbers
        row = current_row

print(f"Row {row} has the most even numbers: {even_numbers}")
