# NOT COMPLETED

# METHOD ONE | USING LINKED LIST IS JUST GREAT
#            | O(1) TIME TO REMOVE AN ELEMENT
#            | O(1) TIME TO ADDED TO THE BEGINNING 
#            | OR THE END   

# METHOD TWO | SORTING - O(N*LOG(N)) TIME

# METHOD THREE | CREATE A NEW LIST

# METHOD FOUR | THE TWO POINTER METHOD

num_elements = int(input())

arr = []

for counter in range(0, num_elements):
    arr.append(int(input()))

ptr_1 = 0
ptr_2 = len(arr) - 1

while(ptr_1 < ptr_2):
    while(arr[ptr_1] < 0):
        ptr_1 += 1
    while(arr[ptr_2] >= 0):
        ptr_2 += -1
    if(arr[ptr_1] >= 0 and arr[ptr_2] < 0 and (ptr_1 < ptr_2)):
        arr[ptr_1], arr[ptr_2] = arr[ptr_2], arr[ptr_1]
        ptr_1 += 1
        ptr_2 -= 1

print(arr)