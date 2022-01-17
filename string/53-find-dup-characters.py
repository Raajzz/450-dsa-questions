# SOLVED | USING MAP 

input_string = input()

count_diction = {}

for string in input_string:
  try:
    count_diction[string] = count_diction[string] + 1
  except:
    count_diction.update({string:1})

dup_chars = []

for key, value in count_diction.items():
  if(value>=2):
    dup_chars.append(key)

print(dup_chars)