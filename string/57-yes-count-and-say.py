# SOLVED |

num_terms = int(input())


input_string = "1"

letter_counter = 0
for i in range(1,num_terms):
  new_string = ""
  letter_counter = 0
  len_input_string = len(input_string)
  for counter in range(0,len_input_string):
    if(counter == 0):
      letter_counter += 1
    elif(input_string[counter] == input_string[counter - 1]):
      letter_counter += 1
    elif((input_string[counter] != input_string[counter - 1])):
      new_string += str(letter_counter) + input_string[counter - 1];
      letter_counter = 1
    if(counter == (len_input_string - 1)):
      new_string += str(letter_counter) + input_string[counter];
  input_string = new_string
  
print(input_string)