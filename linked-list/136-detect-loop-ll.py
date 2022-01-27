# """
# Ideation done.
# Need to work on writing code for condition for
# while loop and while loop statement.

# """

# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# class LinkedList:
#   def __init__(self):
#     self.head = None 

# if __name__ == "__main__":
#     llist = LinkedList()
#     itr_ptr = None

#     print("Enter -1 to end...")
#     get_input = int(input())

#     while(get_input != -1):
#       if(llist.head is None):
#         llist.head = Node(get_input)
#         itr_ptr = llist.head
#       else:
#         itr_ptr.next = Node(get_input)
#         itr_ptr = itr_ptr.next
#       get_input = int(input())
    
    
#     return_check = 0

#     if((llist.head.next is not None) and (llist.head.next.next is not None)):      
#       ptr_once = llist.head
#       ptr_twice = llist.head.next.next
#     else:
#       return_check = 1

#     while((ptr_once is not None) and (ptr_twice is not None) and (ptr_twice.next is not None) and (return_check == 0) ):
#       if(id(ptr_once) == id(ptr_twice)):
#         return_check = 1
    
#     if(return_check == 0):
#       print("Loop does not exist")
#     else:
#       print("Loop exists")

"""
GFG SOLUTION
"""
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # return_check == 0 | NO LOOP
        # return_check == 1 | LOOP
        return_check = 0
        if(head.next is not None):
            if(head.next.next is not None):
                ptr_twice = head.next.next
            else:
                ptr_twice = None
            ptr_once = head
        else:
            ptr_once = head
            ptr_twice = None
          
    
        while(
            (ptr_once is not None) and 
            (ptr_twice is not None) and 
            (ptr_twice.next is not None) and 
            (ptr_twice.next.next is not None) and 
            (return_check == 0) ):
            if(id(ptr_once) == id(ptr_twice)):
                return_check = 1
            ptr_once = ptr_once.next
            ptr_twice = ptr_twice.next.next
        
        if(return_check == 0):
          return False
        else:
          return True
