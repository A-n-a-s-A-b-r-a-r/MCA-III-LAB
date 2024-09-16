import numpy as np 

def odd_rows_even_columns(arr):
    return arr[::2, 1::2]

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

array = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
    array.append(row)

array_np = np.array(array)
print("Odd rows and even columns:\n", odd_rows_even_columns(array_np))
