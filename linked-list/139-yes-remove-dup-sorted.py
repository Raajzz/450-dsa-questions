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
    
  ptr_p = llist.head.next
  ptr_s = llist.head
  
  while(ptr_p is not None):
    if(ptr_p.data != ptr_s.data):
      ptr_p = ptr_p.next
      ptr_s = ptr_s.next
    else:
      ptr_s.next = ptr_p.next
      ptr_t = ptr_p
      ptr_p = ptr_p.next
      del ptr_t
  
  print("Printing the linked-list")
  node_itr = llist.head
  while(node_itr is not None):
    print(node_itr.data)
    node_itr = node_itr.next 