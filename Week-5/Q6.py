import numpy as np

def sort_by_second_row(arr):
    return arr[:, arr[1, :].argsort()]

def sort_by_second_column(arr):
    return arr[arr[:, 1].argsort()]


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

array = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
    array.append(row)
array_np = np.array(array)

print("Sorted by second row:\n", sort_by_second_row(array_np))
print("Sorted by second column:\n", sort_by_second_column(array_np))
