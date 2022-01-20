# NOT SOLVED |

list_1_len = int(input())

list_1 = []

for counter in range(0,list_1_len):
    list_1.append(int(input()))

# METHOD ONE | O(N^2) IMPLEMENTATION
#            | NOT SOLVED

max_val = min(list_1)
min_val = max_val
sum = max_val

for set_size in range(1,list_1_len+1):
    for start in range(0,list_1_len+1):
        if(set_size+start-1 <= list_1_len - 1):
            for counter in range(start,start+set_size):
                sum += list_1[counter]
            if(sum > max_val):
                max_val = sum
            sum = min_val

print(max_val)