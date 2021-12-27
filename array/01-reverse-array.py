n = int(input())
array = []

for i in range(0,n,1):
  array.append(int(input()))

######################################################

# METHOD ONE

arrayReversed = []

for i in range(n-1,-1,-1):
  arrayReversed.append(array[i])

print(arrayReversed)

######################################################

# METHOD TWO

for i in range(0,int(n/2),1):
  array[i], array[(n-1) - i] = array[(n-1) - i], array[i]

for i in array:
  print(i)

######################################################