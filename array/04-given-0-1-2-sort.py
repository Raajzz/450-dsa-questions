# NOT COMPLETED

# METHOD 1 | CREATING A NEW ARRAY AND APPENNDING THE NUMBER OF 
#          | TIMES AN ELEMENT HAD OCCURED.
#          | NOT THE BEST SOLUTION AS AUXILLARY SPACE IS 
#          | O(N)
#          | 

num_elements = int(input())

count = [0,0,0]

elem_list = [0,1,2]

for i in range(0,num_elements,1):
    count[int(input())]+=1

res = []

for i in elem_list:
    for j in range(0,count[i]):
        res.append(i)

print(res)