# COMMON CODE

num_elements = int(input())
list_var = []

for counter in range(0,num_elements,1):
    list_var.append(int(input()))

if(num_elements == 0):
    print("User did not enter any elements!")
    exit()
    
def print_min_max(min, max):
    print("Minimum is " + str(min))
    print("Maximum is " + str(max))


# METHOD ONE | ITERATIVE

if(num_elements == 1):
    print_min_max(list_var[1])
else:
    min_var = list_var[0]
    max_var = list_var[0]
    
    for counter in list_var:
        if(counter < min_var):
            min_var = counter
        elif(counter > max_var):
            max_var = counter
    
    print_min_max(min_var, max_var)

# METHOD TWO | RECURSIVE

def find_min_max(first_param, second_param):
    if(first_param < second_param):
        return [first_param, second_param]
    else:
        return [second_param, first_param]

res = []

def min_max(list_var, start_index, end_index):
    if((end_index - start_index) == 0):
        temp = find_min_max(list_var[start_index],list_var[end_index])
        return temp 
        # redundant, but it follows the style
    elif((end_index - start_index) == 1):
        temp = find_min_max(list_var[start_index],list_var[end_index])
        return temp
    else:
        first_half = min_max(list_var, start_index, int((start_index+end_index)/2))
        second_half = min_max(list_var, int((start_index+end_index)/2)+1, end_index)
        temp = [find_min_max(first_half[0],second_half[0])[0], find_min_max(first_half[1],second_half[1])[1]]
        return temp

res = min_max(list_var, 0, num_elements-1)

print_min_max(res[0],res[1])

# METHOD 3 | COMPARISON IN PAIRS

if(num_elements==1):
    max_var = list_var[0]
    min_var = list_var[0]
elif (num_elements >= 2):
    min_var, max_var = find_min_max(list_var[0],list_var[1])
    for i in range(2, num_elements, 2):
        if(i == num_elements - 1 and num_elements % 2 != 0):
            max_var = find_min_max(max_var, list_var[i])[1]
            min_var = find_min_max(min_var, list_var[i])[0]
        else:
            temp = find_min_max(list_var[i],list_var[i+1])
            max_var = find_min_max(max_var,temp[1])[1]
            min_var = find_min_max(min_var, temp[0])[0]

print_min_max(min_var, max_var)