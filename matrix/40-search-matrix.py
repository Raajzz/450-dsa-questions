# SAMPLE TEST CASES |

matrix = [[1,3,5,7],[7,7,7,7],[23,30,34,60]]
target = 3

row_len = len(matrix)
col_len = len(matrix[0])

row_idx = 100000

for counter in range(row_len):
    if(target <= matrix[counter][col_len - 1] and counter < row_idx):
        row_idx = counter

# YOU'RE MISSING A TEST CASE, WHAT IF row_idx IS NEVER UPDATED?
if(row_idx != 100000):
    for list_element in matrix[row_idx]:
        if(list_element == target):
            print(True)
            exit()
print(False)