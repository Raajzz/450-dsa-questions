# TIME-LIMIT EXCEEDED FOR NON SORTED ARRAYS | BUT SOLVED UNLESS

list_1_len = int(input())

list_1 = []

for counter in range(0,list_1_len):
    list_1.append(int(input()))

list_1.sort()

list_2_len = int(input())

list_2 = []

for counter in range(0,list_2_len):
    list_2.append(int(input()))

list_2.sort()

# METHOD ONE | TWO POINTERS

# UNION

list_res = []
list_res_ints = []

ptr_1 = 0
ptr_2 = 0

while(ptr_1 < list_1_len and ptr_2 < list_2_len):
    if(list_1[ptr_1] < list_2[ptr_2]):
        list_res.append(list_1[ptr_1])
        ptr_1 += 1
    elif(list_2[ptr_2] < list_1[ptr_1]):
        list_res.append(list_2[ptr_2])
        ptr_2 += 1
    else:
        list_res.append(list_1[ptr_1])
        list_res_ints.append(list_1[ptr_1])
        ptr_1 += 1
        ptr_2 += 1

if(ptr_1 == list_1_len):
    while(ptr_2 < list_2_len):
        list_res.append(list_2[ptr_2])
        ptr_2 += 1

if(ptr_2 == list_2_len):
    while(ptr_1 < list_1_len):
        list_res.append(list_1[ptr_1])
        ptr_1 += 1
        
print("Union: " + str(list_res))
print("Union Count: " + str(len(list_res)))
print("Intersection: " + str(list_res_ints))
print("Intersection Count: " + str(len(list_res)))