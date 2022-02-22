class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 

class LinkedList():
  def __init__(self):
    self.head = None 


llist = LinkedList()
itr_ptr = None

print("Enter -1 to end...")
get_input = int(input())

while(get_input != -1):
  if(llist.head is None):
    llist.head = Node(get_input)
    itr_ptr = llist.head
  else:
    itr_ptr.next = Node(get_input)
    itr_ptr = itr_ptr.next
  get_input = int(input())

# We have the linked list inside head

count_0 = 0
count_1 = 0
count_2 = 0

node_ptr = llist.head

while(node_ptr):
  if(node_ptr.data == 0):
    count_0 += 1
  elif(node_ptr.data == 1):
    count_1 += 1
  elif(node_ptr.data == 2):
    count_2 += 1
  node_ptr = node_ptr.next

node_ptr = llist.head

while(node_ptr):
  if(count_0):
    node_ptr.data = 0
    count_0 -= 1
  elif(count_1):
    node_ptr.data = 1
    count_1 -= 1
  elif(count_2):
    node_ptr.data = 2
    count_2 -= 1
  node_ptr = node_ptr.next


node_ptr = llist.head
while(node_ptr):
  print(node_ptr.data)
  node_ptr = node_ptr.next