# SOLVED |

# Take two counters, have a counter that takes the temp_sum_counter and another counter that adds the temp_sum_counter if temp_sum_counter becomes greater than total_sum_counter

# This temp_sum_counter works in a way such that, if the temp_sum_counter if less than 0 then it'll default to 0 | but this process happens after it checks if the value in temp_sum_counter is greater than value in total_sum_counter


INT_MIN = -2147483648

num_elements = int(input())

input_array = []

for counter in range(0, num_elements):
    input_array.append(int(input()))

total_counter = INT_MIN
temp_sum_counter = 0

index = [-1,-1]

new_start_bool = True

for counter in range(0, len(input_array)):
    # This is the meaning of temporary sum
    temp_sum_counter += input_array[counter]
    
    if(total_counter < temp_sum_counter):
        
        total_counter = temp_sum_counter
        
        if(new_start_bool):
            index[0] = -1
            index[1] = -1
        
        if(index[0] == -1):
            index[0] = counter
            index[1] = counter
        else:
            index[1] = counter
        
        new_start_bool = False
    
    # temp because the sum is temporary
    if(temp_sum_counter < 0):
        new_start_bool = True
        temp_sum_counter = 0

print("The maximum sum is", total_counter)
print("Start position:", index[0])
print("End position:", index[1])