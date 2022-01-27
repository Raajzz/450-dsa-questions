diction = {}

arr = [1,2,3,1,2,3,1,2,3]

for element in arr:
  try:
    diction[element] = diction[element] + 1 
  except:
    diction[element] = 1

for key in diction:
  print("Key = ", key, " Value = ", diction[key])

