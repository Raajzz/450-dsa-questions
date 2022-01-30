import math

class Solution:
    def splitList(self, head, head1, head2):
        #code here
        # if(head.next is None):
        #     head1 = head
        #     head0 = head
        # elif(head.next.next is None):
        #     head1 = head
        #     head2 = head.next
        #     head1.next = head1
        #     head2.next = head2
        # else:
        range_ptr = head.next
        head_id = id(head)
        node_count = 1
        
        while(id(range_ptr) != head_id):
            node_count += 1
            range_ptr = range_ptr.next
        del range_ptr
        
        if(node_count == 1):
            head1 = head
            head0 = head
        elif(node_count == 2):
            head1 = head
            head2 = head.next
            head1.next = head1
            head2.next = head2     
        else:
            move_ptr = head
            head1 = head
            half_node_count = math.ceil(node_count/2)
            for counter in range(1, node_count):
                if(counter == half_node_count):
                    head2 = move_ptr.next
                    move_ptr.next = head1
                    move_ptr = head2
                else:
                    move_ptr = move_ptr.next
                    
            move_ptr.next = head2

        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2
