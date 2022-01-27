"""
SOLUTION NOT COMPLETED.

Read the Linked List. When you get a node that is not yet in the 
dictionary then you move ptr_s and ptr_p, if the node is present
then you can move ptr_p to the next node and delete the previous 
node.

"""


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None 

class LinkedList():
  def __init__(self):
    self.head = None 

if __name__ == "__main__":
  llist = LinkedList()
  itr_ptr = None
  
  diction = {}
  
  print("Enter -1 to end...")
  get_input = int(input())

  while(get_input != -1):
    if(llist.head is None):
      llist.head = Node(get_input)
      itr_ptr = llist.head
      try:
        diction[llist.head.data] = diction[llist.head.data] + 1 
      except:
        diction[llist.head.data] = 1
    else:
      itr_ptr.next = Node(get_input)
      try:
        diction[itr_ptr.next.data] = diction[itr_ptr.next.data] + 1 
      except:
        diction[itr_ptr.next.data] = 1
      itr_ptr = itr_ptr.next
    get_input = int(input())
  
  for key in diction:
    print("Key = ", key, " Value = ", diction[key])
