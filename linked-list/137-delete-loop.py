#          | CODE NOT WORKING
#          | USING AUXILLARY SPACE IS NOT ALLOWED

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
    
    ptr_one = None
    ptr_two = None
    
    store_id = {}
    
    if(llist.head is not None):
        if(llist.head.next is not None):
            ptr_one = llist.head.next
            ptr_two = llist.head
        else:
            # return llist.head
            ptr_one = llist.head
            ptr_two = None
    else:
        # return llist.head
        ptr_one = None
        ptr_two = None
    
    while(ptr_one is not None):
        try:
            if(store_id[id(ptr_one)] == 1):
                ptr_two.next = None 
                break
        except:
            store_id[id(ptr_one)] = 1
        
        ptr_two = ptr_one
        ptr_one = ptr_one.next
            
    # return llist.head