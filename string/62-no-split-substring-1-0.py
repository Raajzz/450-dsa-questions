# METHOD 1 |

# NOTE | THERE ARE NO TEST CASES

bin_string = input()
total_count = 0
sub_str_count = 0

for bin_char in bin_string:
  if(sub_str_count == 0):
    inc_char = bin_char
  if(bin_char == inc_char):
    sub_str_count += 1
  else:
    sub_str_count -= 1
  if(sub_str_count == 0):
    total_count += 1
    sub_str_count = 0

if(total_count == 0 or sub_str_count != 0):
  print(-1)
else:
  print(total_count)