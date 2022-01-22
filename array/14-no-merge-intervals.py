# YET TO GET ACCEPTED |
# TLE |

num_elements = int(input())

arr = []

for counter in range(0,num_elements):
  arr.append([int(input()), int(input())])

arr = sorted(arr, key= lambda item: item[0])
res_arr = []

for i in range(0, len(arr)):
  for j in range(i+1, len(arr)):
    if(i != j and arr[i] != [-1,-1] and arr[j] != [-1,-1]):
      
      if(arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]):
        arr[j][0] = -1
        arr[j][1] = -1
      elif(arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][0]):
        arr[i][1] = arr[j][1]
        arr[j][0] = -1
        arr[j][1] = -1

for item in arr:
  if(item != [-1,-1]):
    res_arr.append(item)

print(res_arr)