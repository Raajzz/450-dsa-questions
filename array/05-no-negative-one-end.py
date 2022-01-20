# NOT COMPLETED

# METHOD ONE | USING LINKED LIST IS JUST GREAT
#            | O(1) TIME TO REMOVE AN ELEMENT
#            | O(1) TIME TO ADDED TO THE BEGINNING 
#            | OR THE END   

# METHOD TWO | SORTING - O(N*LOG(N)) TIME

# METHOD THREE | CREATE A NEW LIST

# METHOD FOUR | THE TWO POINTER METHOD

num_elements = int(input())

var_list = []

for i in range(0,num_elements,1):
    var_list.append(int(input()))

print(var_list)
    
ptr_one = 0
ptr_two = (num_elements - 1)

# while(True):
#     if((ptr_one == ptr_two) or (ptr_one>= num_elements) or (ptr_two < 0)):
#         break
#     else:
#         while(var_list[ptr_one] < 0 and (ptr_one < num_elements)):
#             ptr_one += 1
#         while(var_list[ptr_two]>=0 and (ptr_two >= 0)):
#             ptr_two += 1
#         if(var_list[ptr_one] >= 0):
#             var_list[ptr_one], var_list[ptr_two] = \
#             var_list[ptr_two], var_list[ptr_one]
#             ptr_one += 1
#         elif (var_list[ptr_two] < 0):
#             var_list[ptr_one], var_list[ptr_two] = \
#             var_list[ptr_two], var_list[ptr_one]
#             ptr_two += 1

while(True):
    while((ptr_one < num_elements) and (var_list[ptr_one] < 0)):
        ptr_one += 1
    while((ptr_two >= 0) and (var_list[ptr_two]>=0)):
        ptr_two -= 1    
    if((ptr_one >= num_elements) or (ptr_two < 0)):
        break
    var_list[ptr_one], var_list[ptr_two] = var_list[ptr_two], var_list[ptr_one]
    # if((ptr_one >= num_elements) or (ptr_two < 0) or (ptr_one == ptr_two)):
    #     break
    # if(var_list[ptr_one] >= 0):
    #     var_list[ptr_one], var_list[ptr_two] = \
    #     var_list[ptr_two], var_list[ptr_one]
    # elif (var_list[ptr_two] < 0):
    #     var_list[ptr_one], var_list[ptr_two] = \
    #     var_list[ptr_two], var_list[ptr_one]

print(var_list)