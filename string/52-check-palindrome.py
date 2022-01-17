input_string = input()

len_input_string = len(input_string)

for counter in range (0, int(len_input_string/2)):
  if(input_string[counter] != input_string[len_input_string - 1 - counter]):
    print("Not a Palindrome")
    exit()

print("Palindrome")