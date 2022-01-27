"""
Ideation done.
Need to work on writing code for condition for
while loop and while loop statement.

"""

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
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
    
    ptr_once = llist.head
    ptr_twice = llist.head
    
    # while()