class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

if __name__ == "__main__":
  llist = LinkedList()
  # itr_ptr = llist.head
  itr_ptr = None
  get_input = int(input())
  while(get_input):
    if(llist.head is None):
      llist.head = Node(get_input)
      # The below step is important, as you insert something the address changes.
      # Don't treat python variables like C variables
      itr_ptr = llist.head
    else:
      itr_ptr.next = Node(get_input)
      itr_ptr = itr_ptr.next
    get_input = int(input())
  
  end_ptr = llist.head
  if(end_ptr.next is not None):  
    while(end_ptr.next.next is not None):
      end_ptr = end_ptr.next
    
    end_ptr.next.next = llist.head
    llist.head = end_ptr.next
    end_ptr.next = None
  
  node_ptr = llist.head
  while(node_ptr is not None):
    print(node_ptr.data)
    node_ptr = node_ptr.next