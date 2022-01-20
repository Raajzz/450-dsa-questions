# NOT SOLVED |

list_1_len = int(input())

list_1 = []

for counter in range(0,list_1_len):
    list_1.append(int(input()))

next_pos = 0
num_pos = 0

for counter in range(0,list_1_len):
    if(next_pos >= list_1_len or next_pos >= list_1_len-1):
        print(num_pos)
        exit()
    if(counter == next_pos):
        if(list_1[counter] == 0):
            print(-1)
            exit()
        next_pos += list_1[counter]
        num_pos += 1


"""

0
2
3
4

"""