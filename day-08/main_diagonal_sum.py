num_of_rows = int(input("Enter number of rows: "))
num_of_elements = int(input("Enter number of elements: "))

if num_of_rows == num_of_elements:

    print("Enter elements: ")

    matrix = []

    for i in range(num_of_rows):
        lst = []
        for j in range(num_of_elements):
            lst.append(int(input()))
        matrix.append(lst)

    column = 0
    total = 0

    for i in range(num_of_elements):
        for j in range(len(matrix)):
            if column == j:
                total += matrix[i][j]
        column += 1

    print(f"Diagonal sum: {total}")

else:
    print("Matrix must be square")
