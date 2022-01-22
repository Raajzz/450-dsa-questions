# NOT COMPLETED

# METHOD 1 | CREATING A NEW ARRAY AND APPENNDING THE NUMBER OF 
#          | TIMES AN ELEMENT HAD OCCURED.
#          | NOT THE BEST SOLUTION AS AUXILLARY SPACE IS 
#          | O(N)
#          | 

# num_elements = int(input())

# count = [0,0,0]

# elem_list = [0,1,2]

# for i in range(0,num_elements,1):
#     count[int(input())]+=1

# res = []

# for i in elem_list:
#     for j in range(0,count[i]):
#         res.append(i)

# print(res)

# METHOD 1.1 |
# An optimization for the implementation would be to replace the elements in the input array with count*respective_element.

num_elements = int(input())

res_array = []
count_dict = {0:0, 1:0, 2:0}

for counter in range(0, num_elements):
    input_elem = int(input())
    count_dict[input_elem] += 1
    res_array.append(input_elem)

index = 0

for key in count_dict:
    for num_value in range(0,count_dict[key]):
        res_array[index] = key
        index += 1

print(res_array)