list_1_len = int(input())

list_1 = []

for counter in range(0,list_1_len):
    list_1.append(int(input()))

last_element = list_1[list_1_len-1]

# EG: 1 2 3 4 5
#     0 1 2 3 4
# list_1_len = 5
# START WITH THE LAST BEFORE POSITION
# therefore, 'list_1_len-2'

for idx in range(list_1_len-2,-1,-1):
    list_1[idx+1] = list_1[idx]

list_1[0] = last_element

print(list_1)