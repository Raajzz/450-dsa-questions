# METHOD 1 | USE THREE POINTER METHOD FOR REVERSING, USE A SEPERATE POINTER THAT POINTS TO THE START. AFTER YOU REVERSE UPTO A CERTAIN EXTENT AND MAKE THE LAST ELEMENT TO POINT TO THAT FOURTH POINTER AND THEN YOU MOVE THAT POINTER AGAIN TO P. THAT'S IT.

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

  print("Enter reverse position: ")
  rev_pos = int(input())
  
  ptr_p = llist.head.next
  ptr_s = llist.head
  ptr_r = None
  ptr_t = llist.head
  
  counter = 1
  
  while(ptr_p is not None):
    ptr_s.next = ptr_r
    ptr_r = ptr_s
    ptr_s = ptr_p
    ptr_p = ptr_p.next
    counter += 1
    if(counter == rev_pos):
      pass
  # print("Printing the linked-list")
  # node_itr = llist.head
  # while(node_itr is not None):
  #   print(node_itr.data)
  #   node_itr = node_itr.next 