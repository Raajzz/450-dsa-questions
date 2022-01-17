# METHOD 1 | Compare the two strings one by one, have two strings
#          | one as main and other for reseting

input_string = input()
len_is = len(input_string)
input_string_rot = input()
len_isr = len(input_string_rot)

ptr_is = 0
ptr_isr = 0
HOLD_SWITCH_POSITION = -1
match_counter = 0

while(True):
  if( (ptr_isr + 1) % len_isr == HOLD_SWITCH_POSITION):
    if(match_counter != len_isr):
      print("Not Matched")
      break
    else:
      print("Matched")
      break
  else:
    if(input_string[ptr_is] == input_string[ptr_isr]):
      ptr_is += 1
      if(HOLD_SWITCH_POSITION == -1):
        HOLD_SWITCH_POSITION = ptr_isr  
      match_counter += 1
    else:
      ptr_is = 0
      HOLD_SWITCH_POSITION = -1
    ptr_isr = (ptr_isr + 1) % len_isr


# METHOD 2 | Compare the correct_str to the rotated_str, if 
#          | there's a match then increase the pointer, if 
#          | there's no match then rotate the rotated_str and then
#          | continue the process.

