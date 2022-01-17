# SOLVED - LOCAL |
# NOT SOLVED - LEETCODE |

input_string = list(input())

str_size = len(input_string)

for counter in range(0,int(str_size/2)):
  input_string[counter], input_string[str_size - 1 - counter] = \
  input_string[str_size - 1 - counter], input_string[counter]

print(input_string)

